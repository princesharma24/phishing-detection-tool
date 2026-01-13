

A beginner-friendly, rule-based **Phishing Detection Tool** built using Python.  
This tool analyzes a given URL and detects whether it is **SAFE**, **SUSPICIOUS**, or **PHISHING** based on common phishing indicators.

---

## 🔍 What is Phishing?

Phishing is a cyber attack where attackers create fake websites that look real in order to steal:
- Passwords
- Bank details
- OTPs
- Personal information

---

## ⚙️ Features

This tool checks a URL using the following security rules:

1. **URL Length Check**  
   - Very long URLs are suspicious

2. **@ Symbol Detection**  
   - Used to hide real domains

3. **HTTP vs HTTPS**  
   - HTTP URLs are less secure

4. **IP Address in URL**  
   - Phishing sites often use IPs instead of domain names

5. **Suspicious Words Detection**  
   - Words like `login`, `verify`, `bank`, `secure`, etc.

6. **Risk Score Calculation (0–100%)**
   - Generates a final **Verdict**

---

## 🧮 Verdict Logic

| Risk Score | Verdict |
|----------|--------|
| 0–20 | 🟢 SAFE |
| 21–50 | 🟡 SUSPICIOUS |
| 51–100 | 🔴 PHISHING |

---

## ▶️ How to Run

```bash
python detector.py
