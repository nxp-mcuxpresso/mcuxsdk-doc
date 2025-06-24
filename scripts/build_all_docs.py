#!/usr/bin/env python3
"""
Script to build documentation for all boards and then the full documentation.
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
    process_logger.setLevel(logging.DEBUG)  # Set to DEBUG to capture all output
    
    # Remove any existing handlers
    for handler in process_logger.handlers[:]:
        process_logger.removeHandler(handler)
    
    # File handler
    file_handler = logging.FileHandler(log_file,encoding="utf-8", errors="replace")
    file_handler.setLevel(logging.DEBUG)  # Set to DEBUG to capture all output
    
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
    #base_parser = MCUXDoc.add_parser(None)
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Build documentation for all boards and full documentation")
    parser.add_argument("--build_html", action="store_true", help="Build HTML documentation for boards (default: PDF only)")
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
        
        # Log stdout if there's any output
        if process.stdout:
            logger.debug("Command stdout:")
            for line in process.stdout.splitlines():
                logger.debug(f"  {line}")
        
        # Log stderr if there's any output
        if process.stderr:
            logger.debug("Command stderr:")
            for line in process.stderr.splitlines():
                logger.debug(f"  {line}")
        
        return process
    except subprocess.CalledProcessError as e:
        logger.error(f"Command failed with exit code {e.returncode}")
        logger.error(f"Failed command: {' '.join(cmd)}")
        if e.stdout:
            logger.error("Command stdout:")
            for line in e.stdout.splitlines():
                logger.error(f"  {line}")
        if e.stderr:
            logger.error("Command stderr:")
            for line in e.stderr.splitlines():
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
    # Setup board-specific logging
    log_dir = build_dir / "logs"
    board_logger = setup_logging(log_dir, board_target)
    
    try:
        board_logger.info(f"Starting documentation build for board: {board_target}")
        board_build_dir = build_dir / "boards" / board_target
        
        # Ensure build directory exists and is clean
        if board_build_dir.exists():
            board_logger.info(f"Cleaning existing build directory for {board_target}")
            shutil.rmtree(board_build_dir)
        board_build_dir.mkdir(parents=True, exist_ok=True)
        
        # Build PDF documentation
        board_logger.info(f"Building PDF documentation for {board_target}...")
        args.build_dir = str(board_build_dir).replace("\\", "/")
        pdf_cmd = ["west", "doc", "--board", board_target, "pdf"] + mcux_doc.args_to_cmdline(args, ["board", "example_scope"])
        
        pdf_success = False
        html_success = "skipped"
        
        try:

            pdf_path = os.path.join(board_build_dir, 'latex', f'mcuxsdk-{board_target}.pdf')
            min_size_bytes = 1 * 1024 * 1024
            min_size_mb = 1
            max_retries = 3
            for attempt in range(1, max_retries + 1):
                # Run the command
                board_logger.info(f"[Attempt {attempt}] Running PDF generation command: {' '.join(pdf_cmd)}")
                run_command_with_logging(board_logger, pdf_cmd)

                # Check if file exists
                if not os.path.exists(pdf_path):
                    board_logger.error(f"PDF file not found at expected location: {pdf_path}")
                    continue

                # Get file size
                file_size = os.path.getsize(pdf_path)

                board_logger.info(f"Generated PDF size: {file_size / (1024 * 1024):.2f} MB")

                if file_size >= min_size_bytes:
                    board_logger.info("PDF size is acceptable.")
                    break
                else:
                    board_logger.warning(
                        f"PDF size ({file_size / 1024:.2f} KB) < {min_size_mb} MB. Retrying..."
                    )
                    #time.sleep(2)  # Optional: wait before retrying

            board_logger.info(f"PDF documentation for {board_target} built successfully")
            pdf_success = True
            
            # Backup PDF documentation
            if board_build_dir and assets_dir:
                backup_documentation(board_build_dir, assets_dir, board_target, "pdf")
        except subprocess.CalledProcessError as e:
            board_logger.error(f"Error building PDF documentation for {board_target}")
            board_logger.error(f"PDF build failed with exit code: {e.returncode}")
        
        # Build HTML documentation only if --build_html is specified
        if args.build_html:
            board_logger.info(f"Building HTML documentation for {board_target}...")
            html_cmd = ["west", "doc", "--board", board_target, "html"] + mcux_doc.args_to_cmdline(args, ["board"])
            
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
        
        # Return detailed status
        status = {
            board_target: {
                "success": pdf_success and (html_success if args.build_html else True),
                "pdf_success": pdf_success,
                "html_success": html_success
            }
        }
        board_logger.info(f"Build status for {board_target}: {status}")
        return status
        
    except Exception as e:
        board_logger.error(f"Unexpected error processing board {board_target}: {str(e)}")
        board_logger.error(f"Error type: {type(e).__name__}")
        import traceback
        board_logger.error(f"Traceback: {traceback.format_exc()}")
        return {board_target: {"success": False, "error": str(e), "error_type": type(e).__name__}}

def process_full_docs(args, build_dir, assets_dir):
    """Wrapper function for parallel processing of full documentation."""
    # Setup full docs logging
    log_dir = build_dir / "logs"
    full_logger = setup_logging(log_dir, "full")
    
    try:
        full_logger.info("Starting full documentation build")
        full_build_dir = build_dir / "full"
        args.build_dir = str(full_build_dir).replace("\\", "/")
        
        # Build HTML documentation with doxygen
        full_logger.info("Building full HTML documentation with doxygen...")
        html_cmd = ["west", "doc", "html"] + mcux_doc.args_to_cmdline(args, ["board"])
        
        try:
            run_command_with_logging(full_logger, html_cmd)
            full_logger.info("Full HTML documentation built successfully")
            return {"full": True}
        except subprocess.CalledProcessError as e:
            full_logger.error("Error building full HTML documentation")
            return {"full": False}
            
    except Exception as e:
        full_logger.error(f"Unexpected error processing full documentation: {e}")
        return {"full": False}

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
        
        if success:
            status_str = "[OK] Success"
        else:
            status_str = "[FAILED] Failed"
        
        pdf_str = "[OK]" if pdf_status else "[FAILED]"
        html_str = "[OK]" if html_status is True else \
                  "[FAILED]" if html_status is False else \
                  "[SKIPPED]"
        
        logger.info(f"Status: {status_str} (PDF: {pdf_str}, HTML: {html_str})")
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
    main_logger.info(f"Build mode: PDF{' + HTML' if args.build_html else ' only'}")
    
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
    
    # Calculate optimal number of workers (use 50% of available CPU cores to reduce resource contention)
    num_workers = max(1, int(multiprocessing.cpu_count() * 0.5)) + 1
    main_logger.info(f"Using {num_workers} parallel workers")
    
    # Build documentation for boards and full docs in parallel
    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        # Submit all board processing tasks
        future_to_task = {
            executor.submit(process_board, args, board, build_dir, assets_dir): f"board_{board}"
            for board in boards
        }
        
        # Add full docs task
        future_to_task[executor.submit(process_full_docs, args, build_dir, assets_dir)] = "full_docs"
        
        # Collect results as they complete
        for future in concurrent.futures.as_completed(future_to_task):
            task_name = future_to_task[future]
            try:
                result = future.result()
                result_list.append(result)
                if task_name.startswith("board_"):
                    board = task_name[6:]  # Remove "board_" prefix
                    status = result[board]
                    main_logger.info(f"\nCompleted processing board: {board}")
                    print_status(status, main_logger)
                    if isinstance(status, dict) and not status.get('success', False):
                        failed_builds.append((board, status))
                else:
                    main_logger.info("\nCompleted processing full documentation")
                    print_status(result.get('full', {}), main_logger)
                    if isinstance(result.get('full', {}), dict) and not result['full'].get('success', False):
                        failed_builds.append(('full', result['full']))
            except Exception as e:
                main_logger.error(f"\nTask {task_name} generated an exception: {str(e)}")
                main_logger.error(f"Error type: {type(e).__name__}")
                import traceback
                main_logger.error(f"Traceback: {traceback.format_exc()}")
                if task_name.startswith("board_"):
                    board = task_name[6:]
                    error_status = {"success": False, "error": str(e), "error_type": type(e).__name__}
                    result_list.append({board: error_status})
                    failed_builds.append((board, error_status))
                else:
                    error_status = {"success": False, "error": str(e), "error_type": type(e).__name__}
                    result_list.append({"full": error_status})
                    failed_builds.append(('full', error_status))
    
    # move the assets folder to the _build folder
    main_logger.info(f"Move assets from {assets_dir} to {build_dir}/full/html")
    shutil.move(str(assets_dir), str(build_dir/'full'/'html'))

    main_logger.info(f"Move {build_dir}/full/html to {build_dir}/html")
    shutil.move(str(build_dir/'full'/'html'), str(build_dir/'html'))
    
    # Calculate and display build summary
    total_time = time.time() - start_time
    main_logger.info("\n" + "="*80)
    main_logger.info("Build Summary")
    main_logger.info("="*80)
    main_logger.info(f"Total build time: {format_time(total_time)}")
    main_logger.info(f"Total boards processed: {len(boards)}")
    
    if failed_builds:
        main_logger.info(f"\nFailed Builds: {len(failed_builds)}")
        for target, status in failed_builds:
            main_logger.info(f"\nTarget: {target}")
            print_status(status, main_logger)
    else:
        main_logger.info("\nAll builds completed successfully!")
    
    main_logger.info("\n" + "="*80)
    
    return len(failed_builds) == 0

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
