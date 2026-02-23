@echo off
title Intune Hybrid Enrollment Fixer
echo Starting Intune Hybrid Enrollment Fixer...
echo.

:: Check for admin privileges
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo WARNING: Not running as Administrator
    echo Some features may not work properly.
    echo.
    echo Right-click and select "Run as administrator" for full functionality.
    echo.
    pause
)

:: Run the Python script
pythonw.exe intune_hybrid_fixer.py

if errorlevel 1 (
    echo.
    echo Error starting application.
    echo Make sure Python is installed and in PATH.
    echo.
    pause
)
