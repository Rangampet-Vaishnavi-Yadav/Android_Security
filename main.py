import os
import time
import hashlib

# Configuration path for the automatic scanning folder
WATCH_DIRECTORY = "./simulated_downloads"

# 1. Known Malicious Global Hash Database (Simulating VirusTotal's Cloud Registry)
KNOWN_MALICIOUS_HASHES = {
    "44d88612fea8a8f36de82e1278abb2d1": "Trojan.Android.Generic.A",
    "5de4d1a2f6b3c9d8e7f6a5b4c3d2e1f0": "Ransomware.Lockscreen.Android",
    "8b1a9f5d3c7e4b2a1f0e9d8c7b6a5f4e": "Worm.Propagation.Subnet"
}

# 2. Hardcoded Master Threat Matrix (No external JSON file required!)
THREAT_SIGNATURES = {
    "trojan_horses": {
        "keywords": ["backdoor", "remote_shell", "download_exec", "reverse_tcp"],
        "description": "Disguised software that opens unauthorized remote access vectors."
    },
    "logic_bombs_time_bombs": {
        "keywords": ["time.sleep(31536000)", "datetime.now() >", "cron_job_trigger", "delayed_payload"],
        "description": "Malicious code designed to execute after specific conditions or time delays are met."
    },
    "spyware": {
        "keywords": ["keylogger", "dump_contacts", "read_sms_database", "record_audio", "track_gps"],
        "description": "Software designed to silently monitor, intercept, and steal sensitive user data."
    },
    "phishing_links": {
        "keywords": ["secure-login-update", "verify-identity-axis", "free-rewards-claim", "update-credentials"],
        "description": "Deceptive links designed to harvest credentials and sensitive session tokens."
    },
    "worms": {
        "keywords": ["replicate_to_shares", "network_broadcast_payload", "self_propagating", "scan_subnet"],
        "description": "Standalone malware that actively replicates itself to spread across local networks."
    },
    "ransomware": {
        "keywords": ["crypto.encrypt", "ransom_note.txt", "lock_device_screen", "delete_backup_shadow"],
        "description": "Malicious software that encrypts user storage volumes and demands a payout."
    },
    "adware": {
        "keywords": ["inject_popups", "force_redirect_ads", "background_clicker", "monetize_traffic"],
        "description": "Software that aggressively forces unwanted advertisements onto the user."
    },
    "rootkits": {
        "keywords": ["hide_process_id", "modify_system_kernel", "bypass_integrity_check", "hook_system_calls"],
        "description": "Deep system-level tools designed to hide the existence of malware from standard scanners."
    }
}

def calculate_md5(file_path):
    """Generates an MD5 cryptographic fingerprint to match against our virus database."""
    hash_md5 = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except Exception:
        return None

def automated_virustotal_agent():
    print("==============================================================")
    print("🛡️   VIRUSTOTAL-STYLE AUTOMATED DEVICE GUARDIAN ONLINE   🛡️")
    print("==============================================================")
    print(f"[*] Background Daemon Listening to Directory: {WATCH_DIRECTORY}")
    print("[*] Automatically intercepting and scanning all inputs...")
    print("--------------------------------------------------------------")
    
    if not os.path.exists(WATCH_DIRECTORY):
        os.makedirs(WATCH_DIRECTORY)

    scanned_cache = set()

    try:
        while True:
            if not os.path.exists(WATCH_DIRECTORY):
                time.sleep(3)
                continue
                
            current_files = os.listdir(WATCH_DIRECTORY)
            
            for filename in current_files:
                file_path = os.path.join(WATCH_DIRECTORY, filename)
                
                # Scan only new, unread files
                if os.path.isfile(file_path) and file_path not in scanned_cache:
                    print(f"\n[🔍 AUTOMATIC TRIGGER] New file drop detected: {filename}")
                    
                    # PHASE 1: CRYPTOGRAPHIC HASH MATCHING (VirusTotal Method)
                    file_hash = calculate_md5(file_path)
                    if file_hash in KNOWN_MALICIOUS_HASHES:
                        print(f"🚨 ALERT [HASH MATCH]: VirusTotal Registry Database Match!")
                        print(f"  • Classified Variant: {KNOWN_MALICIOUS_HASHES[file_hash]}")
                        print(f"  • File Hash Signature: {file_hash}")
                        scanned_cache.add(file_path)
                        continue
                    
                    # PHASE 2: STATIC BEHAVIORAL CODE ANALYSIS
                    threats_detected = []
                    try:
                        with open(file_path, 'r', errors='ignore') as f:
                            content = f.read().lower()
                            
                        for threat_category, details in THREAT_SIGNATURES.items():
                            for keyword in details["keywords"]:
                                if keyword in content:
                                    threats_detected.append({
                                        "category": threat_category.upper().replace("_", " "),
                                        "trigger": keyword,
                                        "description": details["description"]
                                    })
                    except Exception:
                        pass

                    if threats_detected:
                        print(f"🚨 ALERT [BEHAVIOR MATCH]: Code patterns flagged!")
                        for threat in threats_detected:
                            print(f"  • Rule Category: [{threat['category']}]")
                            print(f"    Indicator: '{threat['trigger']}' -> {threat['description']}")
                    else:
                        print(f"✅ CLEAN: File passed all automated static threat definitions.")
                    
                    scanned_cache.add(file_path)
                    
            time.sleep(3)
            
    except KeyboardInterrupt:
        print("\n[-] Automated Device Guardian terminated.")

if __name__ == "__main__":
    automated_virustotal_agent()