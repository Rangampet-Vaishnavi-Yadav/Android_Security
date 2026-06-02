import os
import json
import time

SIGNATURE_FILE = "signatures.json"

def load_signatures():
    """Loads the comprehensive multi-threat database from the JSON file."""
    if not os.path.exists(SIGNATURE_FILE):
        return {}
    try:
        with open(SIGNATURE_FILE, "r") as f:
            return json.load(f)
    except Exception as e:
        return {}

def universal_threat_scanner(payload_data, data_source="Incoming Stream"):
    """Core Scanning Engine: Evaluates text data against all classified threat sets."""
    signatures = load_signatures()
    threats_detected = []

    for threat_category, details in signatures.items():
        for keyword in details["keywords"]:
            if keyword in payload_data.lower():
                threats_detected.append({
                    "category": threat_category.upper().replace("_", " "),
                    "trigger": keyword,
                    "description": details["description"]
                })

    if threats_detected:
        trigger_system_alert(data_source, threats_detected)
        return False
    else:
        print(f"[✅ CLEAN] {data_source} analyzed. No threat vectors found.")
        return True

def trigger_system_alert(source, threats):
    """Simulates a high-priority Android system notification overlay when an attack is caught."""
    print("\n" + "!" * 60)
    print(f"🚨 ALERT OVERLAY: CRITICAL RISK DETECTED ON DEVICE 🚨")
    print(f"Intercepted Source: {source}")
    print("!" * 60)
    for threat in threats:
        print(f"🛑 TYPE: {threat['category']}")
        print(f"   TRIGGER MATCH: '{threat['trigger']}'")
        print(f"   BEHAVIOR: {threat['description']}")
    print("!" * 60 + "\n")

def run_background_agent():
    """Simulates an Android background daemon service actively intercepting live queues."""
    print("==================================================")
    print("🛡️  ANDROID UNIVERSAL AUTOMATED SECURITY AGENT   🛡️")
    print("==================================================")
    print("[*] Monitoring incoming data streams, files, and QR streams...")
    print("[*] Real-time heuristics initialized. Press Ctrl+C to terminate.")
    print("--------------------------------------------------")
    
    # Simulated stream of incoming files, text, and QR strings landing on the device
    simulated_live_stream = [
        {"data": "Download complete: safe_photo.jpg", "source": "File Manager System"},
        {"data": "http://malicious-portal.com/update-credentials", "source": "SMS Intercept Engine"},
        {"data": "replicate_to_shares and scan_subnet active", "source": "Network Packet Buffer"},
        {"data": "keylogger.start() triggered in background", "source": "App Installation Verification"}
    ]

    try:
        for network_event in simulated_live_stream:
            universal_threat_scanner(network_event["data"], network_event["source"])
            # Mimic real-time interval testing between incoming device interactions
            time.sleep(3)
            
        print("\n[*] Background monitoring pass complete. Engine sitting in ideal state...")
    except KeyboardInterrupt:
        print("\n[-] Automated Security Agent deactivated. Device vulnerable.")

if __name__ == "__main__":
    run_background_agent()