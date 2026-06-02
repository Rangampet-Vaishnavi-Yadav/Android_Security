import os
import time
import hashlib
import json

# Configuration paths for your automated background scanner agent
WATCH_DIRECTORY = "./simulated_downloads"
SIGNATURE_FILE = "signatures.json"

# Known Malicious Global Hash Database (Simulating VirusTotal's backend registry)
KNOWN_MALICIOUS_HASHES = {
    "44d88612fea8a8f36de82e1278abb2d1": "Trojan.Android.Generic.A",
    "5de4d1a2f6b3c9d8e7f6a5b4c3d2e1f0": "Ransomware.Lockscreen.Android",
    "8b1a9f5d3c7e4b2a1f0e9d8c7b6a5f4e": "Worm.Propagation.Subnet"
}

def load_signatures():
    """Loads the comprehensive threat database from the JSON file."""
    if not os.path.exists(SIGNATURE_FILE):
        return {}
    with open(SIGNATURE_FILE, "r") as f:
        return json.load(f)

def calculate_md5(file_path):
    """Generates an MD5 cryptographic fingerprint to match against VirusTotal databases."""
    hash_md5 = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except Exception as e:
        return None

def automated_virustotal_agent():
    print("==============================================================")
    print("🛡️   VIRUSTOTAL-STYLE AUTOMATED DEVICE GUARDIAN ONLINE   🛡️")
    print("==============================================================")
    print(f"[*] Background Daemon Listening to Directory: {WATCH_DIRECTORY}")
    print("[*] Automatically intercepting and scanning all payloads...")
    print("--------------------------------------------------------------")
    
    if not os.path.exists(WATCH_DIRECTORY):
        os.makedirs(WATCH_DIRECTORY)

    signatures = load_signatures()
    scanned_cache = set()

    try:
        while True:
            current_files = os.listdir(WATCH_DIRECTORY)
            
            for filename in current_files:
                file_path = os.path.join(WATCH_DIRECTORY, filename)
                
                # Check if it's a new file that has not been scanned yet
                if os.path.isfile(file_path) and file_path not in scanned_cache:
                    print(f"\n[🔍 AUTOMATIC TRIGGER] New payload intercepted: {filename}")
                    
                    # PHASE 1: CRYPTOGRAPHIC HASH MATCHING (VirusTotal Method)
                    file_hash = calculate_md5(file_path)
                    if file_hash in KNOWN_MALICIOUS_HASHES:
                        print(f"🚨 ALERT [HASH MATCH]: VirusTotal Database Match found!")
                        print(f"  • Classified Variant: {KNOWN_MALICIOUS_HASHES[file_hash]}")
                        print(f"  • File Hash Signature: {file_hash}")
                        scanned_cache.add(file_path)
                        continue
                    
                    # PHASE 2: STATIC BEHAVIORAL ANALYSIS
                    threats_detected = []
                    try:
                        with open(file_path, 'r', errors='ignore') as f:
                            content = f.read().lower()
                            
                        for threat_category, details in signatures.items():
                            for keyword in details["keywords"]:
                                if keyword in content:
                                    threats_detected.append({
                                        "category": threat_category.upper().replace("_", " "),
                                        "trigger": keyword,
                                        "description": details["description"]
                                    })
                    except Exception as e:
                        pass

                    if threats_detected:
                        print(f"🚨 ALERT [BEHAVIOR MATCH]: Deep code signatures flagged!")
                        for threat in threats_detected:
                            print(f"  • Rule Category: [{threat['category']}]")
                            print(f"    Indicator: '{threat['trigger']}' -> {threat['description']}")
                    else:
                        print(f"✅ CLEAN: File passed all VirusTotal database signature checks.")
                    
                    scanned_cache.add(file_path)
                    
            time.sleep(3)
            
    except KeyboardInterrupt:
        print("\n[-] Automated Device Guardian terminated.")

if __name__ == "__main__":
    automated_virustotal_agent()