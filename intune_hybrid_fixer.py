#!/usr/bin/env python3
"""
Intune Hybrid Enrollment & Autopilot Repair Tool
Windows GUI Application

Fixes:
- Broken Hybrid Azure AD Join
- Intune enrollment issues
- Autopilot enrollment problems
- Broken Primary Refresh Tokens (PTRs)
- Certificate issues
- Scheduled task problems
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
import subprocess
import threading
import os
import sys
import re
from datetime import datetime

class IntuneHybridFixer:
    def __init__(self, root):
        self.root = root
        self.root.title("Intune Hybrid Enrollment & Autopilot Repair Tool")
        self.root.geometry("900x700")
        self.root.minsize(800, 600)
        
        # Set icon if available
        try:
            self.root.iconbitmap(default="repair.ico")
        except:
            pass
        
        self.setup_ui()
        self.log_messages = []
        
    def setup_ui(self):
        """Setup the user interface"""
        # Main container
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(2, weight=1)
        
        # Header
        header_frame = ttk.Frame(main_frame)
        header_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        ttk.Label(
            header_frame, 
            text="Intune Hybrid Enrollment & Autopilot Repair Tool",
            font=('Segoe UI', 14, 'bold')
        ).pack(anchor=tk.W)
        
        ttk.Label(
            header_frame,
            text="Fixes Hybrid Azure AD Join, Intune enrollment, Autopilot, and PTR issues",
            font=('Segoe UI', 9)
        ).pack(anchor=tk.W)
        
        # Notebook for tabs
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        
        # Create tabs
        self.create_diagnostics_tab()
        self.create_hybrid_tab()
        self.create_intune_tab()
        self.create_autopilot_tab()
        self.create_ptr_tab()
        self.create_advanced_tab()
        
        # Log area
        log_frame = ttk.LabelFrame(main_frame, text="Operation Log", padding="5")
        log_frame.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        log_frame.columnconfigure(0, weight=1)
        log_frame.rowconfigure(0, weight=1)
        
        self.log_text = scrolledtext.ScrolledText(
            log_frame, 
            wrap=tk.WORD, 
            width=80, 
            height=15,
            font=('Consolas', 9)
        )
        self.log_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=3, column=0, sticky=(tk.W, tk.E))
        
        ttk.Button(
            button_frame, 
            text="Export Log",
            command=self.export_log
        ).pack(side=tk.LEFT, padx=(0, 5))
        
        ttk.Button(
            button_frame,
            text="Clear Log",
            command=self.clear_log
        ).pack(side=tk.LEFT, padx=(0, 5))
        
        ttk.Button(
            button_frame,
            text="Run All Fixes",
            command=self.run_all_fixes
        ).pack(side=tk.RIGHT, padx=(5, 0))
        
        self.status_var = tk.StringVar(value="Ready")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, relief=tk.SUNKEN)
        status_bar.grid(row=4, column=0, sticky=(tk.W, tk.E))
        
    def create_diagnostics_tab(self):
        """Create the diagnostics tab"""
        tab = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(tab, text="Diagnostics")
        
        ttk.Label(
            tab,
            text="System Diagnostics",
            font=('Segoe UI', 11, 'bold')
        ).pack(anchor=tk.W, pady=(0, 10))
        
        diag_frame = ttk.Frame(tab)
        diag_frame.pack(fill=tk.X, pady=(0, 10))
        
        checks = [
            ("Check Hybrid Join Status", self.check_hybrid_join),
            ("Check Intune Enrollment", self.check_intune_status),
            ("Check Autopilot Status", self.check_autopilot_status),
            ("Check Certificates", self.check_certificates),
            ("Check Scheduled Tasks", self.check_scheduled_tasks),
            ("Check Network Connectivity", self.check_network),
            ("Full System Report", self.generate_full_report),
        ]
        
        for text, command in checks:
            btn = ttk.Button(diag_frame, text=text, command=command)
            btn.pack(fill=tk.X, pady=2)
            
    def create_hybrid_tab(self):
        """Create the Hybrid Azure AD Join tab"""
        tab = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(tab, text="Hybrid Join")
        
        ttk.Label(
            tab,
            text="Hybrid Azure AD Join Fixes",
            font=('Segoe UI', 11, 'bold')
        ).pack(anchor=tk.W, pady=(0, 10))
        
        fixes_frame = ttk.Frame(tab)
        fixes_frame.pack(fill=tk.X, pady=(0, 10))
        
        fixes = [
            ("Leave Hybrid Join (dsregcmd /leave)", self.leave_hybrid_join),
            ("Join Hybrid Azure AD", self.join_hybrid_aad),
            ("Force Hybrid Registration", self.force_hybrid_registration),
            ("Clear Hybrid Join Cache", self.clear_hybrid_cache),
            ("Fix Hybrid Join Registry", self.fix_hybrid_registry),
            ("Run dsregcmd /status", self.show_hybrid_status),
        ]
        
        for text, command in fixes:
            btn = ttk.Button(fixes_frame, text=text, command=command)
            btn.pack(fill=tk.X, pady=2)
            
        ttk.Separator(tab, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=10)
        
        ttk.Label(
            tab,
            text="Note: Some operations require elevation. Run as Administrator.",
            foreground="orange",
            font=('Segoe UI', 9, 'italic')
        ).pack(anchor=tk.W)
        
    def create_intune_tab(self):
        """Create the Intune enrollment tab"""
        tab = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(tab, text="Intune")
        
        ttk.Label(
            tab,
            text="Intune Enrollment Fixes",
            font=('Segoe UI', 11, 'bold')
        ).pack(anchor=tk.W, pady=(0, 10))
        
        fixes_frame = ttk.Frame(tab)
        fixes_frame.pack(fill=tk.X, pady=(0, 10))
        
        fixes = [
            ("Unenroll from Intune", self.unenroll_intune),
            ("Re-enroll in Intune", self.reenroll_intune),
            ("Fix Intune Certificates", self.fix_intune_certs),
            ("Reset Intune Client", self.reset_intune_client),
            ("Sync with Intune", self.sync_intune),
            ("Check Enrollment Status", self.check_enrollment_status),
        ]
        
        for text, command in fixes:
            btn = ttk.Button(fixes_frame, text=text, command=command)
            btn.pack(fill=tk.X, pady=2)
            
    def create_autopilot_tab(self):
        """Create the Autopilot tab"""
        tab = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(tab, text="Autopilot")
        
        ttk.Label(
            tab,
            text="Windows Autopilot Fixes",
            font=('Segoe UI', 11, 'bold')
        ).pack(anchor=tk.W, pady=(0, 10))
        
        fixes_frame = ttk.Frame(tab)
        fixes_frame.pack(fill=tk.X, pady=(0, 10))
        
        fixes = [
            ("Clear Autopilot Profile", self.clear_autopilot_profile),
            ("Re-register for Autopilot", self.reregister_autopilot),
            ("Fix Autopilot Registry Keys", self.fix_autopilot_registry),
            ("Reset OOBE", self.reset_oobe),
            ("Check Autopilot Status", self.check_autopilot_status_detailed),
        ]
        
        for text, command in fixes:
            btn = ttk.Button(fixes_frame, text=text, command=command)
            btn.pack(fill=tk.X, pady=2)
            
    def create_ptr_tab(self):
        """Create the PTR (Primary Refresh Token) tab"""
        tab = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(tab, text="PTR Fix")
        
        ttk.Label(
            tab,
            text="Primary Refresh Token (PTR) Fixes",
            font=('Segoe UI', 11, 'bold')
        ).pack(anchor=tk.W, pady=(0, 10))
        
        info_text = """PTRs are used for seamless SSO and device authentication.
Broken PTRs cause: Sign-in prompts, enrollment failures, and auth issues."""
        
        ttk.Label(tab, text=info_text, wraplength=700).pack(anchor=tk.W, pady=(0, 10))
        
        fixes_frame = ttk.Frame(tab)
        fixes_frame.pack(fill=tk.X, pady=(0, 10))
        
        fixes = [
            ("Clear All Tokens (PTA/PRT/Cookies)", self.clear_all_tokens),
            ("Clear Broker Plugin Tokens", self.clear_broker_tokens),
            ("Clear WAM Tokens", self.clear_wam_tokens),
            ("Clear Token Cache", self.clear_token_cache),
            ("Fix CloudAP Plugin", self.fix_cloudap),
            ("Check Token Status", self.check_token_status),
        ]
        
        for text, command in fixes:
            btn = ttk.Button(fixes_frame, text=text, command=command)
            btn.pack(fill=tk.X, pady=2)
            
    def create_advanced_tab(self):
        """Create the advanced fixes tab"""
        tab = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(tab, text="Advanced")
        
        ttk.Label(
            tab,
            text="Advanced Repairs",
            font=('Segoe UI', 11, 'bold')
        ).pack(anchor=tk.W, pady=(0, 10))
        
        fixes_frame = ttk.Frame(tab)
        fixes_frame.pack(fill=tk.X, pady=(0, 10))
        
        fixes = [
            ("Reset Windows Security Center", self.reset_security_center),
            ("Fix MDM Enrollment URL", self.fix_mdm_url),
            ("Reinstall Intune Management Extension", self.reinstall_ime),
            ("Fix Group Policy Sync", self.fix_gp_sync),
            ("Clear Device Registration", self.clear_device_registration),
            ("Nuclear Option (Full Reset)", self.nuclear_reset),
        ]
        
        for text, command in fixes:
            btn = ttk.Button(fixes_frame, text=text, command=command)
            if "Nuclear" in text:
                btn.configure(style="Danger.TButton")
            btn.pack(fill=tk.X, pady=2)
            
        # Create danger style
        style = ttk.Style()
        style.configure("Danger.TButton", foreground="red")
        
    # === DIAGNOSTIC FUNCTIONS ===
    
    def check_hybrid_join(self):
        """Check Hybrid Azure AD Join status"""
        self.log("Checking Hybrid Azure AD Join status...")
        self.run_command("dsregcmd /status", "Hybrid Join Status")
        
    def check_intune_status(self):
        """Check Intune enrollment status"""
        self.log("Checking Intune enrollment status...")
        self.run_command("Get-IntuneManagementExtensionDiagnostics", "Intune Status")
        # Fallback to registry check
        self.run_command('reg query "HKLM\\SOFTWARE\\Microsoft\\Enrollments" /s', "Enrollment Registry")
        
    def check_autopilot_status(self):
        """Check Autopilot status"""
        self.log("Checking Autopilot status...")
        self.run_command("Get-AutopilotDiagnostics", "Autopilot Status")
        
    def check_certificates(self):
        """Check Intune certificates"""
        self.log("Checking certificates...")
        self.run_command('certutil -store -enterprise MY', "Enterprise Certificates")
        
    def check_scheduled_tasks(self):
        """Check Intune scheduled tasks"""
        self.log("Checking scheduled tasks...")
        self.run_command('schtasks /query /fo LIST /v | findstr /i "intune enroll"', "Scheduled Tasks")
        
    def check_network(self):
        """Check network connectivity"""
        self.log("Checking network connectivity...")
        endpoints = [
            "login.microsoftonline.com",
            "device.login.microsoftonline.com",
            "enrollment.manage.microsoft.com",
            "manage.microsoft.com"
        ]
        for endpoint in endpoints:
            self.run_command(f"Test-NetConnection -ComputerName {endpoint} -Port 443 | Select-Object ComputerName, TcpTestSucceeded", f"Network: {endpoint}")
            
    def generate_full_report(self):
        """Generate full diagnostic report"""
        self.log("Generating full system report...")
        self.run_command("dsregcmd /status", "Hybrid Join")
        self.run_command('Get-WmiObject -Namespace "root\\cimv2\\mdm\\dmmap" -Class "MDM_DevDetail_Ext01" | Select-Object DeviceHardwareData', "MDM Info")
        self.check_certificates()
        self.check_scheduled_tasks()
        
    # === HYBRID JOIN FUNCTIONS ===
    
    def leave_hybrid_join(self):
        """Leave Hybrid Azure AD Join"""
        if messagebox.askyesno("Confirm", "This will unjoin the device from Azure AD. Continue?"):
            self.log("Leaving Hybrid Azure AD Join...")
            self.run_command("dsregcmd /leave", "Leave Hybrid Join")
            
    def join_hybrid_aad(self):
        """Join Hybrid Azure AD"""
        self.log("Initiating Hybrid Azure AD Join...")
        self.run_command("dsregcmd /join", "Join Hybrid AAD")
        
    def force_hybrid_registration(self):
        """Force Hybrid registration"""
        self.log("Forcing Hybrid registration...")
        self.run_command("dsregcmd /refreshprt", "Force Registration")
        
    def clear_hybrid_cache(self):
        """Clear Hybrid Join cache"""
        self.log("Clearing Hybrid Join cache...")
        commands = [
            'del /f /q "%localappdata%\\Microsoft\\Windows\\SettingSync\\metastore"',
            'del /f /q "%localappdata%\\Microsoft\\Windows\\SettingSync\\remotemetastore"',
        ]
        for cmd in commands:
            self.run_command(cmd, "Clear Cache")
            
    def fix_hybrid_registry(self):
        """Fix Hybrid Join registry"""
        self.log("Fixing Hybrid Join registry...")
        # Enable Automatic Registration
        self.run_command('reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\WorkplaceJoin" /v autoWorkplaceJoin /t REG_DWORD /d 1 /f', "Enable Auto-Join")
        
    def show_hybrid_status(self):
        """Show detailed Hybrid status"""
        self.check_hybrid_join()
        
    # === INTUNE FUNCTIONS ===
    
    def unenroll_intune(self):
        """Unenroll from Intune"""
        if messagebox.askyesno("Confirm", "This will remove Intune enrollment. Continue?"):
            self.log("Unenrolling from Intune...")
            self.run_command('Get-ChildItem -Path "HKLM:\\SOFTWARE\\Microsoft\\Enrollments" | Remove-Item -Recurse -Force', "Remove Enrollment Keys")
            
    def reenroll_intune(self):
        """Re-enroll in Intune"""
        self.log("Initiating Intune enrollment...")
        self.run_command('deviceenroller.exe /c /AutoEnrollMDM', "Re-enroll Intune")
        
    def fix_intune_certs(self):
        """Fix Intune certificates"""
        self.log("Fixing Intune certificates...")
        # Remove and re-request certificates
        self.run_command('certutil -delstore -enterprise MY "Microsoft Intune MDM Device CA"', "Remove Old Certs")
        
    def reset_intune_client(self):
        """Reset Intune client"""
        self.log("Resetting Intune client...")
        # Stop service, clear cache, restart
        self.run_command('net stop IntuneManagementExtension', "Stop IME")
        self.run_command('rmdir /s /q "C:\\Program Files (x86)\\Microsoft Intune Management Extension\\Policies"', "Clear Cache")
        self.run_command('net start IntuneManagementExtension', "Start IME")
        
    def sync_intune(self):
        """Sync with Intune"""
        self.log("Syncing with Intune...")
        self.run_command('Get-ScheduledTask -TaskName "Microsoft Intune Management Extension" | Start-ScheduledTask', "Sync Intune")
        
    def check_enrollment_status(self):
        """Check enrollment status"""
        self.check_intune_status()
        
    # === AUTOPILOT FUNCTIONS ===
    
    def clear_autopilot_profile(self):
        """Clear Autopilot profile"""
        self.log("Clearing Autopilot profile...")
        self.run_command('reg delete "HKLM:\\SOFTWARE\\Microsoft\\Provisioning\\AutopilotPolicyCache" /f', "Clear Profile Cache")
        
    def reregister_autopilot(self):
        """Re-register for Autopilot"""
        self.log("Re-registering for Autopilot...")
        # Trigger Autopilot enrollment
        self.run_command('Get-ScheduledTask -TaskName "Autopilot" | Start-ScheduledTask', "Trigger Autopilot")
        
    def fix_autopilot_registry(self):
        """Fix Autopilot registry keys"""
        self.log("Fixing Autopilot registry...")
        reg_commands = [
            'reg add "HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\CDJ\\AAD" /v TenantId /t REG_SZ /d "YOUR_TENANT_ID" /f',
            'reg add "HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\CDJ\\AAD" /v TenantName /t REG_SZ /d "YOUR_TENANT.onmicrosoft.com" /f',
        ]
        for cmd in reg_commands:
            self.run_command(cmd, "Fix Registry")
            
    def reset_oobe(self):
        """Reset OOBE"""
        if messagebox.askyesno("Confirm", "This will reset OOBE settings. Continue?"):
            self.log("Resetting OOBE...")
            self.run_command('oobe\\windeploy.exe', "Reset OOBE")
            
    def check_autopilot_status_detailed(self):
        """Check detailed Autopilot status"""
        self.check_autopilot_status()
        
    # === PTR FUNCTIONS ===
    
    def clear_all_tokens(self):
        """Clear all tokens"""
        if messagebox.askyesno("Confirm", "This will clear ALL authentication tokens. User will need to re-authenticate. Continue?"):
            self.log("Clearing all tokens...")
            # Clear all token caches
            self.run_command('klist purge', "Clear Kerberos")
            self.clear_broker_tokens()
            self.clear_wam_tokens()
            self.clear_token_cache()
            
    def clear_broker_tokens(self):
        """Clear Broker Plugin tokens"""
        self.log("Clearing Broker Plugin tokens...")
        paths = [
            '%localappdata%\\Microsoft\\TokenBroker\\Cache',
            '%localappdata%\\Microsoft\\TokenBroker\\tbpqrt',
        ]
        for path in paths:
            self.run_command(f'rmdir /s /q "{path}"', f"Clear {path}")
            
    def clear_wam_tokens(self):
        """Clear WAM tokens"""
        self.log("Clearing WAM tokens...")
        self.run_command('rmdir /s /q "%localappdata%\\Microsoft\\Windows\\AccountsService"', "Clear WAM")
        
    def clear_token_cache(self):
        """Clear token cache"""
        self.log("Clearing token cache...")
        self.run_command('rmdir /s /q "%localappdata%\\Microsoft\\Windows\\SettingSync\\metastore"', "Clear Token Cache")
        
    def fix_cloudap(self):
        """Fix CloudAP plugin"""
        self.log("Fixing CloudAP plugin...")
        self.run_command('wevtutil cl "Microsoft-Windows-CloudAP/Operational"', "Clear CloudAP Logs")
        self.run_command('Restart-Service -Name "CloudAP" -Force', "Restart CloudAP")
        
    def check_token_status(self):
        """Check token status"""
        self.log("Checking token status...")
        self.run_command('dsregcmd /status | findstr /i "prt"', "PRT Status")
        
    # === ADVANCED FUNCTIONS ===
    
    def reset_security_center(self):
        """Reset Windows Security Center"""
        self.log("Resetting Security Center...")
        self.run_command('Restart-Service -Name "wscsvc" -Force', "Restart WSC")
        
    def fix_mdm_url(self):
        """Fix MDM enrollment URL"""
        self.log("Fixing MDM enrollment URL...")
        self.run_command('reg add "HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows\\CurrentVersion\\MDM" /v DisableRegistrationPollOnLoginTask /t REG_DWORD /d 0 /f', "Fix MDM URL")
        
    def reinstall_ime(self):
        """Reinstall Intune Management Extension"""
        self.log("Reinstalling IME...")
        # Download and reinstall IME
        self.run_command('powershell -Command "Invoke-WebRequest -Uri https://portal.manage.microsoft.com/api/download/IME -OutFile C:\\temp\\IME.exe; Start-Process C:\\temp\\IME.exe -Wait"', "Reinstall IME")
        
    def fix_gp_sync(self):
        """Fix Group Policy sync"""
        self.log("Fixing Group Policy sync...")
        self.run_command('gpupdate /force', "Force GP Update")
        
    def clear_device_registration(self):
        """Clear device registration"""
        self.log("Clearing device registration...")
        self.run_command('reg delete "HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\CDJ" /f', "Clear CDJ")
        
    def nuclear_reset(self):
        """Nuclear option - full reset"""
        if messagebox.askyesno("⚠️ WARNING", "This will perform a COMPLETE reset of all Intune/Hybrid/Autopilot settings. The device may need to be re-enrolled. Continue?"):
            self.log("Executing nuclear reset...")
            self.leave_hybrid_join()
            self.unenroll_intune()
            self.clear_device_registration()
            self.clear_all_tokens()
            self.clear_autopilot_profile()
            messagebox.showinfo("Complete", "Nuclear reset complete. Please restart the device and re-enroll.")
            
    def run_all_fixes(self):
        """Run all common fixes"""
        if messagebox.askyesno("Run All Fixes", "This will run all diagnostic and repair operations. Continue?"):
            self.log("Running all fixes...")
            self.generate_full_report()
            self.fix_hybrid_registry()
            self.fix_mdm_url()
            self.sync_intune()
            self.fix_gp_sync()
            messagebox.showinfo("Complete", "All fixes applied. Please restart the device.")
            
    # === UTILITY FUNCTIONS ===
    
    def run_command(self, command, description):
        """Run a PowerShell command and log output"""
        self.log(f"\n{'='*60}")
        self.log(f"Operation: {description}")
        self.log(f"Command: {command}")
        self.log(f"{'='*60}")
        
        def execute():
            try:
                result = subprocess.run(
                    ["powershell", "-Command", command],
                    capture_output=True,
                    text=True,
                    shell=False,
                    timeout=120
                )
                
                output = result.stdout if result.stdout else "(no output)"
                error = result.stderr if result.stderr else ""
                
                self.log(f"Output:\n{output}")
                if error:
                    self.log(f"Errors:\n{error}")
                    
                if result.returncode == 0:
                    self.log("✓ Success")
                else:
                    self.log(f"✗ Failed (exit code: {result.returncode})")
                    
            except subprocess.TimeoutExpired:
                self.log("✗ Command timed out")
            except Exception as e:
                self.log(f"✗ Error: {str(e)}")
                
            self.log("")
            
        # Run in separate thread to keep UI responsive
        thread = threading.Thread(target=execute)
        thread.start()
        
    def log(self, message):
        """Add message to log"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        self.log_messages.append(log_entry)
        
        # Update UI in main thread
        self.root.after(0, self._update_log_ui, log_entry)
        
    def _update_log_ui(self, message):
        """Update log UI (called from main thread)"""
        self.log_text.insert(tk.END, message)
        self.log_text.see(tk.END)
        self.status_var.set("Working..." if "Operation:" in message else "Ready")
        
    def export_log(self):
        """Export log to file"""
        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
            initialfile=f"intune_repair_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        )
        if filename:
            with open(filename, 'w') as f:
                f.writelines(self.log_messages)
            messagebox.showinfo("Exported", f"Log saved to {filename}")
            
    def clear_log(self):
        """Clear log display"""
        self.log_text.delete(1.0, tk.END)
        self.log_messages.clear()
        

def main():
    """Main entry point"""
    # Check for admin privileges
    try:
        import ctypes
        is_admin = ctypes.windll.shell32.IsUserAnAdmin()
    except:
        is_admin = False
        
    root = tk.Tk()
    
    if not is_admin:
        # Show warning but still run
        warning = tk.Toplevel(root)
        warning.title("Warning")
        warning.geometry("400x150")
        ttk.Label(
            warning, 
            text="⚠️ Not running as Administrator",
            font=('Segoe UI', 10, 'bold'),
            foreground="orange"
        ).pack(pady=10)
        ttk.Label(
            warning,
            text="Some operations require elevation.\nRight-click and 'Run as Administrator' for best results.",
            wraplength=350
        ).pack(pady=5)
        ttk.Button(warning, text="Continue Anyway", command=warning.destroy).pack(pady=10)
        warning.transient(root)
        warning.grab_set()
        root.wait_window(warning)
    
    app = IntuneHybridFixer(root)
    root.mainloop()


if __name__ == "__main__":
    main()
