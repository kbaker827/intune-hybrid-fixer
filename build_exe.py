#!/usr/bin/env python3
"""
Build standalone executable using PyInstaller
Usage: python build_exe.py
"""

import subprocess
import sys
import os

def build():
    """Build standalone executable"""
    print("Building standalone executable...")
    
    # Check for PyInstaller
    try:
        import PyInstaller
    except ImportError:
        print("PyInstaller not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
    
    # Build command
    cmd = [
        "pyinstaller",
        "--onefile",           # Single executable
        "--windowed",          # No console window
        "--name", "IntuneHybridFixer",
        "--icon", "repair.ico",  # Icon if available
        "--add-data", "repair.ico;.",  # Include icon
        "intune_hybrid_fixer.py"
    ]
    
    print(f"Running: {' '.join(cmd)}")
    subprocess.call(cmd)
    
    print("\nBuild complete!")
    print("Executable location: dist/IntuneHybridFixer.exe")

if __name__ == "__main__":
    build()
