import os
import json

SIGNATURE_FILE = "signatures.json"

def load_signatures():
    """Loads the threat database from the JSON file."""
    if not os.path.exists(SIGNATURE_FILE):
        print(f"❌ Error: {SIGNATURE_FILE} not found. Please create it first.")
        return {}
    try:
        with open(SIGNATURE_FILE, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"❌ Error reading threat database: {e}")
        return {}

def scan_input_data(data_to_scan, input_type="Text/Link"):
    """Scans any string data (links, text, or QR payload) against all threat rules."""
    print(f"\n[🔍 AUTOMATIC SCAN] Analyzing incoming {input_type}...")
    
    signatures = load_signatures()
    threats_found = []

    # Loop through every threat category in our database
    for threat_type, details in signatures.items():
        for keyword in details["keywords"]:
            if keyword in data_to_scan.lower():
                threats_found.append(f"🚨 ALERT: Detected [{threat_type.upper()}] indicator -> '{keyword}' ({details['description']})")

    if threats_found:
        for threat in threats_found:
            print(threat)
        return False
    else:
        print(f"✅ {input_type} passed all threat database signature checks.")
        return True

if __name__ == "__main__":
    print("=== MULTI-THREAT SECURITY ENGINE ONLINE ===")
    
    # Simulation 1: Testing a suspected Time Bomb signature
    scan_input_data("if datetime.now() > trigger_date: execute_payload()", "Code Script")
    
    # Simulation 2: Testing a suspected Trojan horse signature
    scan_input_data("http://example-link.com/download_exec", "URL Link")