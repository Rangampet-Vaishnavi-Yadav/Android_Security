import os
import re

def analyze_link(url):
    """Scans a link for suspicious indicators like phishing keywords or IP-based URLs."""
    print(f"\n[🔍 LINK SCAN] Analyzing URL: {url}")
    
    # Common phishing keywords or suspicious top-level domains
    suspicious_indicators = ["malware", "phishing", "free-login", "verify-account", "update-password"]
    
    # Check for suspicious keywords
    for indicator in suspicious_indicators:
        if indicator in url.lower():
            return f"🚨 ALERT: Suspicious keyword '{indicator}' found in URL!"
            
    # Check if the URL uses an IP address instead of a domain name (common in phishing)
    ip_pattern = r"https?://\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    if re.match(ip_pattern, url):
        return "🚨 ALERT: URL uses a raw IP address instead of a standard domain name!"
        
    return "✅ Link passed basic security checks."


def analyze_file(file_path):
    """Inspects a file extension and its content for known signature keywords."""
    print(f"\n[📁 FILE SCAN] Inspecting file path: {file_path}")
    
    if not os.path.exists(file_path):
        return "❌ Error: File does not exist at specified path."
        
    # Flag high-risk executable or script extensions
    filename = os.path.basename(file_path)
    if filename.endswith(('.exe', '.apk', '.bat', '.sh', '.vbs')):
        return f"🚨 ALERT: Dangerous file extension detected: {filename}"
        
    # Scan text content for signature keywords
    try:
        with open(file_path, 'r', errors='ignore') as f:
            content = f.read().lower()
            if "eval(" in content or "base64_decode" in content or "malware_payload" in content:
                return "🚨 ALERT: Suspicious code patterns or signature keywords found inside file!"
    except Exception as e:
        return f"⚠️ Notice: Unable to read file content ({str(e)}). Extension check only."

    return "✅ File passed basic structure analysis."


def analyze_qr_data(qr_text):
    """Analyzes the text or payload extracted from a decoded QR code."""
    print(f"\n[📷 QR SCAN] Analyzing extracted QR data payload...")
    
    if not qr_text.strip():
        return "❌ Error: QR code payload is empty."
        
    # If the QR code contains a URL, pass it to the link scanner
    if qr_text.startswith(("http://", "https://")):
        print("[*] QR code contains a link. Redirecting to Link Analyzer...")
        return analyze_link(qr_text)
        
    # Check for hidden command patterns or exploit text inside raw data
    suspicious_commands = ["drop", "exec", "sudo", "system("]
    for cmd in suspicious_commands:
        if cmd in qr_text.lower():
            return f"🚨 ALERT: Suspicious automated command pattern found in QR code: '{cmd}'"
            
    return "✅ QR data payload looks clean."


# Global testing runner to see how they evaluate inputs
if __name__ == "__main__":
    print("=== SECURITY ENGINES WORKING ===")
    
    # 1. Test the Link Scan
    link_result = analyze_link("http://192.168.1.100/verify-account")
    print(link_result)
    
    # 2. Test the QR Scan
    qr_result = analyze_qr_data("https://phishing-login-portal.xyz")
    print(qr_result)