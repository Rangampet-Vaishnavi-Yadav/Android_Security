import os
import json

SIGNATURE_FILE = "signatures.json"

def load_signatures():
    """Loads the comprehensive multi-threat database from the JSON file."""
    if not os.path.exists(SIGNATURE_FILE):
        print(f"❌ Error: {SIGNATURE_FILE} not found. Please verify its path.")
        return {}
    try:
        with open(SIGNATURE_FILE, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"❌ Error reading threat database: {e}")
        return {}

def universal_threat_scanner(payload_data, data_source="Incoming Stream"):
    """
    Core Scanning Engine: Evaluates text data against all classified 
    threat sets (Worms, Ransomware, Adware, Spyware, Trojans, etc.)
    """
    print(f"\n[🔍 AUTOMATIC SCAN] Inspecting {data_source}...")
    
    signatures = load_signatures()
    threats_detected = []

    # Iterate through all threat classes dynamically
    for threat_category, details in signatures.items():
        for keyword in details["keywords"]:
            if keyword in payload_data.lower():
                threats_detected.append({
                    "category": threat_category.upper().replace("_", " "),
                    "trigger": keyword,
                    "description": details["description"]
                })

    # Output detailed analytical results
    if threats_detected:
        print(f"🚨 ALERT: Risk identified in {data_source}!")
        for threat in threats_detected:
            print(f"  • Category: [{threat['category']}]")
            print(f"    Indicator Caught: '{threat['trigger']}'")
            print(f"    Details: {threat['description']}\n")
        return False
    else:
        print(f"✅ Clean: {data_source} passed all threat definitions successfully.")
        return True

if __name__ == "__main__":
    print("==================================================")
    print("🛡️   UNIVERSAL MULTI-CLASS THREAT ENGINE ONLINE   🛡️")
    print("==================================================")
    
    # 1. Simulating a Ransomware script check
    universal_threat_scanner("file.write(crypto.encrypt(user_data))", "Downloaded File: document_patch.py")
    
    # 2. Simulating a Worm payload check
    universal_threat_scanner("run_network_broadcast_payload()", "Network Data Packets")
    
    # 3. Simulating an Adware link check
    universal_threat_scanner("http://ad-server.xyz/inject_popups", "QR Code Embedded Link")