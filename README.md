# Intune Hybrid Enrollment & Autopilot Repair Tool

A Windows GUI application for fixing broken Hybrid Azure AD Join, Intune enrollment, Autopilot, and Primary Refresh Token (PTR) issues.

## Features

### 🔍 Diagnostics
- Check Hybrid Join Status (dsregcmd)
- Check Intune Enrollment
- Check Autopilot Status
- Check Certificates
- Check Scheduled Tasks
- Network Connectivity Tests
- Full System Report

### 🔧 Hybrid Azure AD Join Fixes
- Leave Hybrid Join
- Join Hybrid Azure AD
- Force Hybrid Registration
- Clear Hybrid Join Cache
- Fix Hybrid Registry Keys
- Show Hybrid Status

### 📱 Intune Enrollment Fixes
- Unenroll from Intune
- Re-enroll in Intune
- Fix Intune Certificates
- Reset Intune Client
- Sync with Intune
- Check Enrollment Status

### 🚀 Windows Autopilot Fixes
- Clear Autopilot Profile
- Re-register for Autopilot
- Fix Autopilot Registry Keys
- Reset OOBE (Out of Box Experience)
- Check Autopilot Status

### 🔐 Primary Refresh Token (PTR) Fixes
- Clear All Tokens (Kerberos, Broker, WAM)
- Clear Broker Plugin Tokens
- Clear WAM Tokens
- Clear Token Cache
- Fix CloudAP Plugin
- Check Token Status

### ⚡ Advanced Repairs
- Reset Windows Security Center
- Fix MDM Enrollment URL
- Reinstall Intune Management Extension
- Fix Group Policy Sync
- Clear Device Registration
- Nuclear Option (Complete Reset)

## Requirements

- Windows 10/11
- Python 3.7+ (for source)
- Administrator privileges (recommended)

## Installation

### Option 1: Run from Source
1. Install Python 3.7+ from python.org
2. Download this tool
3. Double-click `run_fixer.bat` or run:
   ```
   python intune_hybrid_fixer.py
   ```

### Option 2: Standalone Executable
1. Install PyInstaller: `pip install pyinstaller`
2. Run: `python build_exe.py`
3. Find `IntuneHybridFixer.exe` in `dist/` folder

## Usage

1. **Run as Administrator** (right-click → Run as administrator)
2. Select the appropriate tab:
   - **Diagnostics** - Check current status
   - **Hybrid Join** - Fix Azure AD Join issues
   - **Intune** - Fix MDM enrollment
   - **Autopilot** - Fix Autopilot enrollment
   - **PTR Fix** - Fix authentication tokens
   - **Advanced** - Advanced repairs
3. Click the desired operation button
4. Review the operation log
5. Export logs if needed for support

## Common Issues Fixed

### Hybrid Join Issues
- Device showing "Pending" in Azure AD
- SSO not working
- "Work or school account" problems
- Certificate issues

### Intune Enrollment Issues
- Device not enrolling in Intune
- "Something went wrong" errors
- Certificate enrollment failures
- Policy sync issues

### Autopilot Issues
- Autopilot profile not applying
- Device stuck in OOBE
- Enrollment status page errors
- White glove deployment failures

### PTR Issues
- Constant re-authentication prompts
- SSO not working
- "Your organization requires you to sign in again"
- Teams/Outlook authentication loops

## Warning

⚠️ **Some operations are destructive:**
- "Leave Hybrid Join" removes Azure AD join
- "Unenroll from Intune" removes MDM enrollment
- "Nuclear Option" clears ALL settings
- "Clear All Tokens" requires re-authentication

Always export logs before major operations.

## Log Export

Click "Export Log" to save operation logs. These are useful for:
- Troubleshooting
- Microsoft Support cases
- Documentation
- Audit trails

## Technical Details

The tool uses PowerShell commands to:
- `dsregcmd` - Manage device registration
- Registry edits - Fix configuration issues
- Certificate management - Fix cert problems
- Service management - Restart Windows services
- File system operations - Clear caches

## Troubleshooting

### "Python not found"
Install Python 3.7+ and check "Add Python to PATH" during installation.

### "Access Denied" errors
Run as Administrator (right-click → Run as administrator).

### Changes not taking effect
Restart the device after major operations.

### Still having issues
1. Run the "Full System Report" diagnostic
2. Export the log
3. Contact Microsoft Support with the log

## Safety Features

- Confirmation dialogs for destructive operations
- Operation logging with timestamps
- Export logs for review
- Non-destructive diagnostics available
- Clear labeling of dangerous operations

## License

MIT License - Free to use and modify

## Author

Created for IT Administrators managing Hybrid Azure AD Join, Intune, and Autopilot deployments.
