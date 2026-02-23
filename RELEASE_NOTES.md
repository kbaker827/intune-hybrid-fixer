# Intune Hybrid Enrollment & Autopilot Repair Tool v1.0.0

**The all-in-one Windows GUI tool for IT administrators to fix broken Hybrid Azure AD Join, Intune enrollment, Autopilot, and Primary Refresh Token (PTR) issues.**

---

## 🎯 What This Tool Does

If you've ever spent hours troubleshooting why a Windows device won't:
- Complete Hybrid Azure AD Join (stuck on "Pending")
- Enroll in Microsoft Intune MDM
- Apply Windows Autopilot profiles
- Maintain seamless SSO (single sign-on)
- Stop prompting users for authentication

...then this tool is for you.

---

## ✨ Key Features

### 6 Diagnostic & Repair Categories

| Tab | Purpose | Operations |
|-----|---------|------------|
| **🔍 Diagnostics** | System assessment | Hybrid status, Intune enrollment, Autopilot state, certificates, network tests |
| **🔧 Hybrid Join** | Azure AD Join fixes | Leave/join Hybrid AAD, force registration, clear cache, fix registry |
| **📱 Intune** | MDM enrollment fixes | Unenroll/reenroll, fix certificates, reset client, force sync |
| **🚀 Autopilot** | OOBE & deployment fixes | Clear profiles, re-register, fix registry, reset OOBE |
| **🔐 PTR Fix** | Authentication token fixes | Clear Kerberos/Broker/WAM tokens, fix CloudAP |
| **⚡ Advanced** | Deep repairs | Security Center reset, MDM URL fix, IME reinstall, ☢️ nuclear reset |

### 30+ Repair Operations

Every common fix is one click away:
- `dsregcmd /leave` and `/join` operations
- Certificate store cleanup
- Token cache clearing
- Registry key fixes
- Scheduled task resets
- Network connectivity verification

### Built for IT Pros

- **Detailed logging** - Every operation timestamped and logged
- **Export logs** - Save logs for Microsoft Support cases
- **Safety confirmations** - Destructive operations require confirmation
- **Admin detection** - Warns if not running as Administrator
- **PowerShell backend** - Uses native Windows commands

---

## 🚀 Getting Started

### Option 1: Run from Python
1. Install Python 3.7+ on Windows
2. Download this release
3. Double-click `run_fixer.bat`

### Option 2: Build Standalone EXE
```batch
pip install pyinstaller
python build_exe.py
```
Find `IntuneHybridFixer.exe` in the `dist/` folder.

---

## 📋 Common Use Cases

### Device Stuck on "Pending" in Azure AD
1. Go to **Hybrid Join** tab
2. Click "Leave Hybrid Join"
3. Click "Join Hybrid Azure AD"
4. Restart device

### Intune Enrollment Keeps Failing
1. Go to **Intune** tab
2. Click "Fix Intune Certificates"
3. Click "Sync with Intune"

### Autopilot Profile Won't Apply
1. Go to **Autopilot** tab
2. Click "Clear Autopilot Profile"
3. Click "Re-register for Autopilot"

### Users Get Constant Sign-In Prompts
1. Go to **PTR Fix** tab
2. Click "Clear All Tokens"
3. User signs in once

---

## ⚠️ Important Notes

### Requires Elevation
**Run as Administrator** for best results. The tool will warn you if not running elevated.

### Destructive Operations
Some operations are destructive (leave Hybrid Join, unenroll Intune, clear tokens). Always export logs before major operations.

### No External Dependencies
Uses only Python standard library + tkinter. No pip installs needed.

---

## 📝 What's Included

- `intune_hybrid_fixer.py` - Main GUI application (664 lines)
- `run_fixer.bat` - Windows batch launcher
- `build_exe.py` - PyInstaller build script
- `requirements.txt` - Dependencies (stdlib only)

---

## 📊 System Requirements

- Windows 10 (1809+) or Windows 11
- Python 3.7+ (for running from source)
- Administrator privileges (recommended)

---

## 📄 License

MIT License - Free to use, modify, and distribute.

---

**Happy Troubleshooting! 🛠️**
