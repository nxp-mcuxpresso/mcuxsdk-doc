'''MCUXpresso Document Build All Script
   Copyright 2025 NXP
   All rights reserved.

   SPDX-License-Identifier: BSD-3-Clause
'''
#!/usr/bin/env python3
"""
Script to build documentation for all boards and then the full documentation.
Supports multiple doxygen modes coexisting in the same build.
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path
import argparse
import time
import logging
from west_commands import mcux_doc
import concurrent.futures
from concurrent.futures import ProcessPoolExecutor
import multiprocessing
from datetime import datetime
import yaml

# Import path validation module
script_dir = Path(__file__).parent
sys.path.insert(0, str(script_dir))
from validate_paths import PathValidator

logger = logging.getLogger(__name__)

def setup_logging(log_dir, board_name=None):
    """Setup logging configuration for a specific board or the main process."""
    log_dir = Path(log_dir)
    log_dir.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    if board_name:
        log_file = log_dir / f"board_{board_name}_{timestamp}.log"
    else:
        log_file = log_dir / f"main_{timestamp}.log"
    
    # Create a new logger for this process
    process_logger = logging.getLogger(f"board_{board_name}" if board_name else "main")
    process_logger.setLevel(logging.DEBUG)
    
    # Remove any existing handlers
    for handler in process_logger.handlers[:]:
        process_logger.removeHandler(handler)
    
    # File handler
    file_handler = logging.FileHandler(log_file, encoding="utf-8", errors="replace")
    file_handler.setLevel(logging.DEBUG)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # Add handlers
    process_logger.addHandler(file_handler)
    process_logger.addHandler(console_handler)
    
    return process_logger

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Build documentation for all boards and full documentation")
    parser.add_argument("--build_html", action="store_true", help="Build HTML documentation for boards (default: PDF only)")
    parser.add_argument("--pdf_only", action="store_true", help="Build board PDFs only, skip full HTML docs (for parallel CI)")
    return mcux_doc.add_new_arguments(parser).parse_args()

def find_all_boards(docs_dir):
    """Find all boards in the documentation."""
    boards = []
    for family_dir in (docs_dir / "boards").glob("*/"):
        family = family_dir.name
        for board_dir in family_dir.glob("*/"):
            if board_dir.is_dir() and (board_dir / "index.rst").exists():
                board_name = board_dir.name
                boards.append(board_name)
    
    return sorted(boards)

def get_optimal_worker_count(build_mode, low_memory=False):
    """Calculate optimal number of workers based on build mode and memory constraints."""
    cpu_count = multiprocessing.cpu_count()

    if low_memory:
        # Low memory mode: very conservative
        return max(1, int(cpu_count * 0.25))
    else:
        return max(1, int(cpu_count * 0.5))


def backup_documentation(build_dir, assets_dir, board_target=None, doc_type="html"):
    """Backup generated documentation to assets directory."""
    # Create assets directory if it doesn't exist
    assets_dir.mkdir(parents=True, exist_ok=True)
    
    if board_target:
        # Board-specific documentation
        if doc_type == "html":
            # Backup HTML documentation
            board_html_dir = build_dir / "html"
            board_assets_dir = assets_dir / "boards" / board_target.replace("/", "_") / "html"
            
            # Remove existing backup if it exists
            if board_assets_dir.exists():
                shutil.rmtree(board_assets_dir)
            
            # Create parent directories
            board_assets_dir.parent.mkdir(parents=True, exist_ok=True)
            
            # Copy HTML documentation
            if board_html_dir.exists():
                shutil.copytree(board_html_dir, board_assets_dir)
                logger.info(f"Backed up HTML documentation for {board_target} to {board_assets_dir}")
            else:
                logger.info(f"Warning: HTML documentation for {board_target} not found at {board_html_dir}")
        
        elif doc_type == "pdf":
            # Backup PDF documentation
            board_pdf_file = build_dir / "latex" / f"mcuxsdk-{board_target}.pdf"
            board_assets_pdf = assets_dir / "boards" / board_target / f"mcuxsdk-{board_target}.pdf"
            
            # Create parent directories
            board_assets_pdf.parent.mkdir(parents=True, exist_ok=True)
            
            # Copy PDF documentation
            if board_pdf_file.exists():
                shutil.copy2(board_pdf_file, board_assets_pdf)
                logger.info(f"Backed up PDF documentation for {board_target} to {board_assets_pdf}")
            else:
                logger.info(f"Warning: PDF documentation for {board_target} not found at {board_pdf_file}")
    else:
        # Full documentation
        if doc_type == "html":
            # Backup HTML documentation
            html_dir = build_dir / "html"
            full_assets_dir = assets_dir / "html"
            
            # Remove existing backup if it exists
            if full_assets_dir.exists():
                shutil.rmtree(full_assets_dir)
            
            # Copy HTML documentation
            if html_dir.exists():
                shutil.copytree(html_dir, full_assets_dir)
                logger.info(f"Backed up full HTML documentation to {full_assets_dir}")
            else:
                logger.info(f"Warning: Full HTML documentation not found at {html_dir}")
        
        elif doc_type == "pdf":
            # Backup PDF documentation
            pdf_file = build_dir / "latex" / "mcuxsdk.pdf"
            full_assets_pdf = assets_dir / "mcuxsdk.pdf"
            
            # Copy PDF documentation
            if pdf_file.exists():
                shutil.copy2(pdf_file, full_assets_pdf)
                logger.info(f"Backed up full PDF documentation to {full_assets_pdf}")
            else:
                logger.info(f"Warning: Full PDF documentation not found at {pdf_file}")

def run_command_with_logging(logger, cmd, check=True):
    """Run a command and log its output."""
    logger.info(f"Executing command: {' '.join(cmd)}")
    
    try:
        # Add environment information to help diagnose issues
        logger.info(f"System memory: {get_system_memory_info()}")
        logger.info(f"Current working directory: {os.getcwd()}")
        
        process = subprocess.run(
            cmd,
            check=check,
            capture_output=True,
            text=True,
            encoding='utf-8'
        )

        # Log stdout to file only (debug level)
        if process.stdout:
            logger.debug("Command stdout:")
            for line in process.stdout.splitlines():
                logger.debug(f"  {line}")

        # Log stderr to file; only errors/warnings to console
        if process.stderr:
            logger.debug("Command stderr:")
            for line in process.stderr.splitlines():
                logger.debug(f"  {line}")

        return process
    except subprocess.CalledProcessError as e:
        logger.error(f"Command failed with exit code {e.returncode}")
        logger.error(f"Failed command: {' '.join(cmd)}")
        # Log full stdout/stderr to file at debug level.
        if e.stdout:
            for line in e.stdout.splitlines():
                logger.debug(f"  {line}")
        if e.stderr:
            for line in e.stderr.splitlines():
                logger.debug(f"  {line}")
        # Print the last 30 lines of stderr to console as error context.
        # This avoids fragile keyword matching — stderr from a failed build
        # naturally contains the error cause at the end (sphinx traceback,
        # cmake error, latexmk failure message, etc).
        stderr_lines = (e.stderr or '').splitlines()
        tail = [l for l in stderr_lines[-30:] if l.strip()]
        if tail:
            logger.error("Last lines of stderr:")
            for line in tail:
                logger.error(f"  {line}")
        # Add system state at time of failure
        logger.error(f"System state at failure - Memory: {get_system_memory_info()}")
        raise

def get_system_memory_info():
    """Get current system memory information."""
    try:
        import psutil
        mem = psutil.virtual_memory()
        return f"Total: {mem.total / (1024*1024*1024):.1f}GB, Available: {mem.available / (1024*1024*1024):.1f}GB, Used: {mem.percent}%"
    except ImportError:
        return "Memory info not available (psutil not installed)"

def process_board(args, board_target, build_dir, assets_dir):
    """Wrapper function for parallel processing of board documentation."""
    board_start = time.time()

    # Setup board-specific logging
    log_dir = build_dir / "logs"
    board_logger = setup_logging(log_dir, board_target)

    try:
        board_logger.info(f"Starting documentation build for board: {board_target}")
        board_logger.info(f"Driver build mode: {args.build_mode}")
        if args.low_memory:
            board_logger.info("Low memory mode enabled")

        board_build_dir = build_dir / "boards" / board_target

        # Ensure build directory exists and is clean
        if board_build_dir.exists():
            board_logger.info(f"Cleaning existing build directory for {board_target}")
            shutil.rmtree(board_build_dir)
        board_build_dir.mkdir(parents=True, exist_ok=True)

        # Build PDF documentation
        board_logger.info(f"Building PDF documentation for {board_target}...")
        args.build_dir = str(board_build_dir).replace("\\", "/")

        # Prepare command with build mode options
        base_cmd = ["west", "doc", "--board", board_target]
        if args.build_mode != 'original':
            base_cmd.extend(["--build_mode", args.build_mode])
        if args.low_memory:
            base_cmd.append("--low_memory")

        pdf_cmd = base_cmd + ["pdf"] + mcux_doc.args_to_cmdline(args, ["board", "example_scope", "build_mode", "low_memory"])

        pdf_success = False
        needs_retry = False
        html_success = "skipped"

        try:
            pdf_path = os.path.join(board_build_dir, 'latex', f'mcuxsdk-{board_target}.pdf')
            min_size_bytes = 1 * 1024 * 1024

            board_logger.info(f"[Attempt 1] Running PDF generation command: {' '.join(pdf_cmd)}")
            run_command_with_logging(board_logger, pdf_cmd)

            # Check if file exists and size
            if not os.path.exists(pdf_path):
                board_logger.error(f"PDF file not found at expected location: {pdf_path}")
                needs_retry = True
            else:
                file_size = os.path.getsize(pdf_path)
                board_logger.info(f"Generated PDF size: {file_size / (1024 * 1024):.2f} MB")

                if file_size >= min_size_bytes:
                    board_logger.info("PDF size is acceptable.")
                    pdf_success = True
                else:
                    board_logger.warning(
                        f"PDF size ({file_size / 1024:.2f} KB) < 1 MB. Will retry in second pass."
                    )
                    needs_retry = True

            if pdf_success:
                board_logger.info(f"PDF documentation for {board_target} built successfully")
                # Backup PDF documentation
                if board_build_dir and assets_dir:
                    backup_documentation(board_build_dir, assets_dir, board_target, "pdf")

        except subprocess.CalledProcessError as e:
            board_logger.error(f"Error building PDF documentation for {board_target}")
            board_logger.error(f"PDF build failed with exit code: {e.returncode}")
            # Read the LaTeX log for detailed error info — latexmk errors
            # are often not propagated through cmake/sphinx stderr
            _print_latex_errors(board_logger, board_build_dir, board_target)

        # Build HTML documentation only if --build_html is specified
        if args.build_html:
            board_logger.info(f"Building HTML documentation for {board_target}...")
            html_cmd = base_cmd + ["html"] + mcux_doc.args_to_cmdline(args, ["board", "build_mode", "low_memory"])

            try:
                run_command_with_logging(board_logger, html_cmd)
                board_logger.info(f"HTML documentation for {board_target} built successfully")
                html_success = True

                # Backup HTML documentation
                if board_build_dir and assets_dir:
                    backup_documentation(board_build_dir, assets_dir, board_target, "html")
            except subprocess.CalledProcessError as e:
                board_logger.error(f"Error building HTML documentation for {board_target}")
                board_logger.error(f"HTML build failed with exit code: {e.returncode}")
                html_success = False
        else:
            board_logger.info(f"Skipping HTML documentation build for {board_target} (--build_html not specified)")

        duration = time.time() - board_start

        # Return detailed status
        status = {
            board_target: {
                "success": pdf_success and (html_success if args.build_html else True),
                "pdf_success": pdf_success,
                "html_success": html_success,
                "needs_retry": needs_retry,
                "build_mode": args.build_mode,
                "duration_sec": duration,
            }
        }
        board_logger.info(f"Build completed in {format_time(duration)}")
        board_logger.info(f"Build status for {board_target}: {status}")
        return status

    except Exception as e:
        board_logger.error(f"Unexpected error processing board {board_target}: {str(e)}")
        board_logger.error(f"Error type: {type(e).__name__}")
        import traceback
        board_logger.error(f"Traceback: {traceback.format_exc()}")
        duration = time.time() - board_start
        return {board_target: {"success": False, "error": str(e), "error_type": type(e).__name__,
                               "build_mode": args.build_mode, "duration_sec": duration}}


def _print_latex_errors(logger, board_build_dir, board_target):
    """Read the LaTeX log file and print error lines to console.

    LaTeX errors (lines starting with !) and context lines are often not
    propagated through cmake/sphinx, so we read them directly from the
    .log file that latexmk produces.
    """
    latex_log = board_build_dir / 'latex' / f'mcuxsdk-{board_target}.log'
    if not latex_log.exists():
        # Try generic name
        for log_file in (board_build_dir / 'latex').glob('*.log'):
            latex_log = log_file
            break
    if not latex_log.exists():
        return

    try:
        with open(latex_log, 'r', encoding='utf-8', errors='replace') as f:
            lines = f.readlines()

        # Collect LaTeX error blocks: lines starting with ! and a few
        # lines of context after each
        error_blocks = []
        i = 0
        while i < len(lines):
            line = lines[i]
            if line.startswith('!'):
                # Capture the error line + up to 5 context lines
                block = [line.rstrip()]
                for j in range(1, 6):
                    if i + j < len(lines):
                        ctx = lines[i + j].rstrip()
                        block.append(ctx)
                        if ctx.startswith('l.'):  # LaTeX line number
                            break
                error_blocks.append(block)
                i += len(block)
            else:
                i += 1

        if error_blocks:
            logger.error(f"LaTeX errors from {latex_log.name}:")
            for block in error_blocks[:10]:  # Limit to first 10 errors
                for line in block:
                    logger.error(f"  {line}")
                logger.error("")  # blank line between errors
    except Exception:
        pass  # Don't fail the build over log parsing


def _check_build_errors(process):
    """Check if a command that exited with code 0 actually had build errors.

    west doc with --keep-going may return 0 even when sphinx or latexmk
    encountered fatal errors.  Scan stderr/stdout for indicators.
    """
    errors = []
    for output in (process.stderr or '', process.stdout or ''):
        for line in output.splitlines():
            upper = line.upper()
            if any(kw in upper for kw in [
                'FATAL ERROR', 'EXTENSION ERROR', 'THEME ERROR',
                'SEVERE:', 'LATEXMK: FAILURE',
            ]):
                errors.append(line.strip())
    return errors


def process_full_docs(args, build_dir, assets_dir):
    """Wrapper function for parallel processing of full documentation."""
    # Setup full docs logging
    log_dir = build_dir / "logs"
    full_logger = setup_logging(log_dir, "full")

    try:
        full_logger.info("Starting full documentation build")
        full_logger.info(f"Driver build mode: {args.build_mode}")
        full_logger.info("Note: Non-driver projects use their configured mode from user_config.yml")
        if args.low_memory:
            full_logger.info("Low memory mode enabled")

        full_build_dir = build_dir / "full"
        args.build_dir = str(full_build_dir).replace("\\", "/")

        # Build HTML documentation with doxygen
        full_logger.info("Building full HTML documentation with doxygen...")

        # Prepare command with build mode options
        base_cmd = ["west", "doc"]
        if args.build_mode != 'original':
            base_cmd.extend(["--build_mode", args.build_mode])
        if args.low_memory:
            base_cmd.append("--low_memory")

        html_cmd = base_cmd + ["html"] + mcux_doc.args_to_cmdline(args, ["board", "build_mode", "low_memory"])

        try:
            result = run_command_with_logging(full_logger, html_cmd)
            # Check for hidden build errors even on exit code 0
            build_errors = _check_build_errors(result)
            if build_errors:
                full_logger.error("Full HTML build returned 0 but contains errors:")
                for err in build_errors:
                    full_logger.error(f"  {err}")
                return {"full": {"success": False, "build_mode": args.build_mode,
                                 "error": "; ".join(build_errors[:5])}}
            full_logger.info("Full HTML documentation built successfully")
            return {"full": {"success": True, "build_mode": args.build_mode}}
        except subprocess.CalledProcessError as e:
            full_logger.error("Error building full HTML documentation")
            return {"full": {"success": False, "build_mode": args.build_mode}}

    except Exception as e:
        full_logger.error(f"Unexpected error processing full documentation: {e}")
        return {"full": {"success": False, "error": str(e), "build_mode": args.build_mode}}

def format_time(seconds):
    """Format time in seconds to a human-readable string."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    if hours > 0:
        return f"{hours}h {minutes}m {seconds}s"
    elif minutes > 0:
        return f"{minutes}m {seconds}s"
    else:
        return f"{seconds}s"

def print_status(status, logger):
    """Print build status with ASCII characters."""
    if isinstance(status, dict):
        success = status.get('success', False)
        pdf_status = status.get('pdf_success', False)
        html_status = status.get('html_success', 'skipped')
        build_mode = status.get('build_mode', 'unknown')
        
        if success:
            status_str = "[OK] Success"
        else:
            status_str = "[FAILED] Failed"
        
        pdf_str = "[OK]" if pdf_status else "[FAILED]"
        html_str = "[OK]" if html_status is True else \
                  "[FAILED]" if html_status is False else \
                  "[SKIPPED]"
        
        logger.info(f"Status: {status_str} (PDF: {pdf_str}, HTML: {html_str}, Driver Mode: {build_mode})")
        if not success and 'error' in status:
            logger.error(f"Error: {status['error']}")
    else:
        status_str = "[OK] Success" if status else "[FAILED] Failed"
        logger.info(f"Status: {status_str}")

def main():
    """Main entry point."""
    start_time = time.time()
    args = parse_args()
    
    # Define paths
    docs_dir = Path(__file__).absolute().parents[1]
    build_dir = docs_dir / args.build_dir
    assets_dir = docs_dir / args.build_dir / "_assets"
    result_list = []
    failed_builds = []
    
    # Setup main logging
    log_dir = build_dir / "logs"
    main_logger = setup_logging(log_dir)
    main_logger.info("Starting documentation build process")
    main_logger.info(f"Driver build mode: {args.build_mode}")
    main_logger.info(f"Build type: PDF{' + HTML' if args.build_html else ' only'}")
    main_logger.info("Note: Non-driver projects use their 'mode' setting from user_config.yml")
    main_logger.info("Note: Multiple doxygen modes can coexist in the same build")
    if args.low_memory:
        main_logger.info("Low memory mode: Enabled")
    
    # Log system information at start
    main_logger.info(f"System information:")
    main_logger.info(f"CPU cores: {multiprocessing.cpu_count()}")
    main_logger.info(f"Memory: {get_system_memory_info()}")
    
    # Create assets directory if it doesn't exist
    if assets_dir.exists():
        shutil.rmtree(assets_dir)
    assets_dir.mkdir(parents=True, exist_ok=True)
    
    # Determine which boards to build
    main_logger.info(mcux_doc.args_to_cmdline(args))
    if args.board:
        boards = [args.board]
    else:
        boards = find_all_boards(docs_dir)
    
    main_logger.info(f"Found {len(boards)} boards to build")
    
    # Calculate optimal number of workers based on build mode
    num_workers = get_optimal_worker_count(args.build_mode, args.low_memory)
    main_logger.info(f"Using {num_workers} parallel workers (optimized for {args.build_mode} mode)")
    main_logger.info(f"CPU cores: {multiprocessing.cpu_count()}")

    # Phase 1: Build all board PDFs in parallel
    # Board PDFs run first so the full HTML docs build (which is memory-heavy
    # due to 100 doxygen projects + sphinx -j auto) gets all system resources.
    main_logger.info("Phase 1: Building board PDFs")
    board_phase_start = time.time()
    retry_boards = []

    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        future_to_board = {
            executor.submit(process_board, args, board, build_dir, assets_dir): board
            for board in boards
        }

        for future in concurrent.futures.as_completed(future_to_board):
            board = future_to_board[future]
            try:
                result = future.result()
                result_list.append(result)
                status = result[board]
                main_logger.info(f"\nCompleted processing board: {board}")
                print_status(status, main_logger)
                if isinstance(status, dict):
                    if status.get('needs_retry'):
                        retry_boards.append(board)
                        main_logger.info(f"Board {board} queued for retry (small PDF)")
                    elif not status.get('success', False):
                        failed_builds.append((board, status))
            except Exception as e:
                main_logger.error(f"\nBoard {board} generated an exception: {str(e)}")
                main_logger.error(f"Error type: {type(e).__name__}")
                import traceback
                main_logger.error(f"Traceback: {traceback.format_exc()}")
                error_status = {"success": False, "error": str(e), "error_type": type(e).__name__, "build_mode": args.build_mode}
                result_list.append({board: error_status})
                failed_builds.append((board, error_status))

    board_phase_time = time.time() - board_phase_start
    main_logger.info(f"\nBoard PDF phase completed in {format_time(board_phase_time)}")

    # Phase 2: Retry boards that produced small PDFs
    if retry_boards:
        main_logger.info(f"\nRetrying {len(retry_boards)} boards with small PDFs: {retry_boards}")
        retry_start = time.time()
        max_retries = 2

        with ProcessPoolExecutor(max_workers=num_workers) as executor:
            for retry_attempt in range(1, max_retries + 1):
                if not retry_boards:
                    break
                main_logger.info(f"Retry attempt {retry_attempt} for {len(retry_boards)} boards")
                future_to_board = {
                    executor.submit(process_board, args, board, build_dir, assets_dir): board
                    for board in retry_boards
                }
                still_need_retry = []
                for future in concurrent.futures.as_completed(future_to_board):
                    board = future_to_board[future]
                    try:
                        result = future.result()
                        result_list.append(result)
                        status = result[board]
                        main_logger.info(f"\nRetry completed for board: {board}")
                        print_status(status, main_logger)
                        if isinstance(status, dict):
                            if status.get('needs_retry'):
                                still_need_retry.append(board)
                            elif not status.get('success', False):
                                failed_builds.append((board, status))
                    except Exception as e:
                        main_logger.error(f"\nRetry for {board} generated an exception: {str(e)}")
                        error_status = {"success": False, "error": str(e), "build_mode": args.build_mode}
                        result_list.append({board: error_status})
                        failed_builds.append((board, error_status))
                retry_boards = still_need_retry

        # Any boards still failing after retries are failures
        for board in retry_boards:
            failed_builds.append((board, {"success": False, "error": "PDF too small after retries", "build_mode": args.build_mode}))

        main_logger.info(f"Retry phase completed in {format_time(time.time() - retry_start)}")

    # Phase 3: Build full HTML documentation
    # Runs after board PDFs complete so it gets all system memory and CPU.
    # The full docs build is memory-intensive (100 doxygen projects + sphinx
    # with parallel workers), running it concurrently with boards risks OOM.
    if args.pdf_only:
        main_logger.info("\nSkipping full HTML build (--pdf_only mode)")
    else:
        main_logger.info("\nPhase 3: Building full HTML documentation")
        full_result = process_full_docs(args, build_dir, assets_dir)
        result_list.append(full_result)
        main_logger.info("\nCompleted processing full documentation")
        print_status(full_result.get('full', {}), main_logger)
        if isinstance(full_result.get('full', {}), dict) and not full_result['full'].get('success', False):
            failed_builds.append(('full', full_result['full']))

    # Move the assets folder to the _build folder
    main_logger.info(f"Move assets from {assets_dir} to {build_dir}/full/html")
    if assets_dir.exists() and (build_dir / 'full').exists():
        shutil.move(str(assets_dir), str(build_dir/'full'/'html'))

        main_logger.info(f"Move {build_dir}/full/html to {build_dir}/html")
        if (build_dir/'full'/'html').exists():
            shutil.move(str(build_dir/'full'/'html'), str(build_dir/'html'))
    
    # Validate paths in the generated HTML output
    main_logger.info("\n" + "="*80)
    main_logger.info("Running Path Validation Checks")
    main_logger.info("="*80)
    
    html_output_dir = build_dir / 'html'
    if html_output_dir.exists():
        main_logger.info(f"Validating HTML output in: {html_output_dir}")
        validator = PathValidator(html_output_dir)
        
        try:
            is_valid = validator.scan_directory()
            
            if is_valid:
                main_logger.info("✓ Path validation PASSED: No prohibited characters found in HTML paths")
            else:
                main_logger.error("✗ Path validation FAILED: Prohibited characters found in HTML paths")
                main_logger.error("Please review the validation errors above and fix the source files")
                main_logger.error(f"Prohibited characters: {validator.PROHIBITED_CHARS}")
                # Add to failed builds
                failed_builds.append(('path_validation', {
                    'success': False,
                    'error': 'HTML paths contain prohibited characters',
                    'build_mode': args.build_mode
                }))
        except Exception as e:
            main_logger.error(f"Error during path validation: {str(e)}")
            import traceback
            main_logger.error(f"Traceback: {traceback.format_exc()}")
            failed_builds.append(('path_validation', {
                'success': False,
                'error': f'Path validation error: {str(e)}',
                'build_mode': args.build_mode
            }))
    else:
        main_logger.warning(f"HTML output directory not found: {html_output_dir}")
        main_logger.warning("Skipping path validation")
    
    main_logger.info("="*80 + "\n")
    
    # Calculate and display build summary
    total_time = time.time() - start_time
    main_logger.info("\n" + "="*80)
    main_logger.info("Build Summary")
    main_logger.info("="*80)
    main_logger.info(f"Driver build mode: {args.build_mode}")
    main_logger.info(f"Non-driver projects: Use 'mode' from user_config.yml")
    main_logger.info(f"Multiple modes coexist: Yes")
    if args.low_memory:
        main_logger.info("Low memory mode: Enabled")
    main_logger.info(f"Total build time: {format_time(total_time)}")
    main_logger.info(f"Total boards processed: {len(boards)}")
    main_logger.info(f"Parallel workers used: {num_workers}")
    
    # Per-board timing summary
    board_durations = []
    for result in result_list:
        for name, status in result.items():
            if isinstance(status, dict) and 'duration_sec' in status:
                board_durations.append((status['duration_sec'], name))
    if board_durations:
        board_durations.sort(reverse=True)
        main_logger.info(f"\nBoard Build Times (top 10 slowest):")
        for dur, name in board_durations[:10]:
            main_logger.info(f"  {name:35s} {format_time(dur)}")
        if len(board_durations) > 1:
            avg = sum(d for d, _ in board_durations) / len(board_durations)
            main_logger.info(f"  {'Average':35s} {format_time(avg)}")
            main_logger.info(f"  {'Median':35s} {format_time(sorted(d for d, _ in board_durations)[len(board_durations)//2])}")

    if failed_builds:
        main_logger.info(f"\nFailed Builds: {len(failed_builds)}")
        for target, status in failed_builds:
            main_logger.info(f"\nTarget: {target}")
            print_status(status, main_logger)
    else:
        main_logger.info("\nAll builds completed successfully!")
    
    # Build mode specific summary
    main_logger.info(f"\n=== Build Mode Summary ===")
    main_logger.info(f"Driver Projects Mode: {args.build_mode}")
    if args.build_mode == 'html':
        main_logger.info(f"- Driver doxygen HTML generated directly")
        main_logger.info(f"- Driver API documentation: {build_dir}/html/api/")
        main_logger.info(f"- Memory usage optimized for drivers")
    elif args.build_mode == 'sphinx':
        main_logger.info(f"- Separate Sphinx projects for each driver device")
        main_logger.info(f"- Driver device projects: device_projects/")
        main_logger.info(f"- Cross-references use intersphinx")
    elif args.build_mode == 'original':
        main_logger.info(f"- Using breathe for driver Doxygen XML integration")
        main_logger.info(f"- Single Sphinx build process for drivers")
    
    main_logger.info(f"\nNon-Driver Projects:")
    main_logger.info(f"- Each project uses its 'mode' setting from user_config.yml")
    main_logger.info(f"- Can be 'breathe', 'html', or 'sphinx' independently")
    main_logger.info(f"- All modes coexist in the same build")
    
    main_logger.info("\n" + "="*80)
    
    return len(failed_builds) == 0

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
