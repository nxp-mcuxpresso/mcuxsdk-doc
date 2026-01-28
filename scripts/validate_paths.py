#!/usr/bin/env python3
"""
Path Security Validator for Sphinx Documentation

This script validates that HTML-generated documentation paths do not contain
characters that pose security risks as identified by IT security findings.

Prohibited characters: "$%();<>?[]`{|}

Usage:
    python validate_paths.py <build_dir>
    
    Where <build_dir> is the path to the Sphinx HTML build directory (e.g., _build/html)

Exit codes:
    0 - No prohibited characters found
    1 - Prohibited characters found in paths
    2 - Error during execution
"""

import os
import sys
import re
from pathlib import Path
from typing import List, Tuple, Set

# Prohibited characters as per IT security policy
PROHIBITED_CHARS = r'[$%();<>?\[\]`{|}]'
PROHIBITED_CHARS_DISPLAY = '"$%();<>?[]`{|}'

class PathValidator:
    """Validates paths against security policy."""
    
    def __init__(self, build_dir: Path):
        """
        Initialize the validator.
        
        Args:
            build_dir: Path to the HTML build directory
        """
        self.build_dir = build_dir
        self.violations: List[Tuple[str, str]] = []
        self.prohibited_pattern = re.compile(PROHIBITED_CHARS)
        
    def find_prohibited_chars(self, path: str) -> Set[str]:
        """
        Find all prohibited characters in a path.
        
        Args:
            path: The path string to check
            
        Returns:
            Set of prohibited characters found
        """
        return set(self.prohibited_pattern.findall(path))
    
    def validate_path(self, file_path: Path) -> bool:
        """
        Validate a single file path.
        
        Args:
            file_path: Path to validate
            
        Returns:
            True if path is valid, False if it contains prohibited characters
        """
        # Get relative path from build directory
        try:
            rel_path = file_path.relative_to(self.build_dir)
        except ValueError:
            # Path is not relative to build_dir, skip it
            return True
            
        path_str = str(rel_path)
        
        # Check for prohibited characters
        prohibited = self.find_prohibited_chars(path_str)
        
        if prohibited:
            self.violations.append((path_str, ''.join(sorted(prohibited))))
            return False
            
        return True
    
    def scan_directory(self) -> bool:
        """
        Recursively scan the build directory for paths with prohibited characters.
        
        Returns:
            True if all paths are valid, False if any violations found
        """
        if not self.build_dir.exists():
            print(f"Error: Build directory '{self.build_dir}' does not exist.", file=sys.stderr)
            return False
            
        if not self.build_dir.is_dir():
            print(f"Error: '{self.build_dir}' is not a directory.", file=sys.stderr)
            return False
        
        print(f"Scanning documentation paths in: {self.build_dir}")
        print(f"Checking for prohibited characters: {PROHIBITED_CHARS_DISPLAY}")
        print("-" * 80)
        
        # Walk through all files and directories
        for root, dirs, files in os.walk(self.build_dir):
            root_path = Path(root)
            
            # Check directory names
            for dir_name in dirs:
                dir_path = root_path / dir_name
                self.validate_path(dir_path)
            
            # Check file names
            for file_name in files:
                file_path = root_path / file_name
                self.validate_path(file_path)
        
        return len(self.violations) == 0
    
    def report(self) -> None:
        """Print validation report."""
        if not self.violations:
            print("\n✓ SUCCESS: No prohibited characters found in paths.")
            print(f"  Total paths scanned in: {self.build_dir}")
            return
        
        print(f"\n✗ FAILURE: Found {len(self.violations)} path(s) with prohibited characters:\n")
        
        # Group violations by prohibited character for better reporting
        violations_by_char = {}
        for path, chars in self.violations:
            for char in chars:
                if char not in violations_by_char:
                    violations_by_char[char] = []
                violations_by_char[char].append(path)
        
        # Print violations grouped by character
        for char in sorted(violations_by_char.keys()):
            paths = violations_by_char[char]
            print(f"Character '{char}' found in {len(paths)} path(s):")
            for path in sorted(paths):
                print(f"  - {path}")
            print()
        
        print("-" * 80)
        print("POLICY VIOLATION:")
        print("SDK HTML-generated documentation must not contain the following")
        print(f"characters in paths due to security risk findings: {PROHIBITED_CHARS_DISPLAY}")
        print("-" * 80)
        print("\nRecommendations:")
        print("1. Rename files/directories to remove prohibited characters")
        print("2. Update source .rst/.md files that generate these paths")
        print("3. Check Doxygen output if paths are from API documentation")
        print("4. Review Sphinx configuration for custom path generation")


def main():
    """Main entry point."""
    if len(sys.argv) != 2:
        print("Usage: python validate_paths.py <build_dir>", file=sys.stderr)
        print("Example: python validate_paths.py _build/html", file=sys.stderr)
        sys.exit(2)
    
    build_dir = Path(sys.argv[1])
    
    try:
        validator = PathValidator(build_dir)
        is_valid = validator.scan_directory()
        validator.report()
        
        sys.exit(0 if is_valid else 1)
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(2)


if __name__ == '__main__':
    main()
