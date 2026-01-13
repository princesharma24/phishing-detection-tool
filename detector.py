
import re

url = input("Enter a URL: ")
risk_score = 0

print("\nChecking URL...")
print("URL:", url)

# Rule 1: URL length
if len(url) > 75:
    print("⚠️ URL is very long")
    risk_score += 20
else:
    print("✅ URL length looks normal")

# Rule 2: @ symbol
if "@" in url:
    print("⚠️ '@' symbol found")
    risk_score += 25
else:
    print("✅ No '@' symbol")

# Rule 3: HTTPS
if url.startswith("https://"):
    print("✅ HTTPS detected")
else:
    print("⚠️ Not using HTTPS")
    risk_score += 15

# Rule 4: IP address
ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
if re.search(ip_pattern, url):
    print("⚠️ IP address detected")
    risk_score += 25
else:
    print("✅ No IP address")

# Rule 5: Suspicious words
suspicious_words = [
    "login", "verify", "update", "secure",
    "account", "bank", "confirm", "signin"
]

url_lower = url.lower()
found_words = 0

for word in suspicious_words:
    if word in url_lower:
        print(f"⚠️ Suspicious word → {word}")
        risk_score += 5
        found_words += 1

if found_words == 0:
    print("✅ No suspicious words")

# FINAL RESULT
print("\n🔐 Final Risk Score:", risk_score, "%")

if risk_score <= 20:
    print("🟢 Verdict: SAFE")
elif risk_score <= 50:
    print("🟡 Verdict: SUSPICIOUS")
else:
    print("🔴 Verdict: PHISHING")
