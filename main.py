# Define the link we want to check
test_url = "http://example.com"

# Display a status message
print("Scanning links...")
print("Checking for threats...")

# Simple check for suspicious keywords
if "malware" in test_url or "phishing" in test_url:
    print("Warning: Potential threat detected!")
else:
    print("Link looks clean.") 