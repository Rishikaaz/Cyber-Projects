import re

def is_phishing(url):
    suspicious_keywords = ['login', 'verify', 'update', 'banking']
    if url.count('.') > 3 or '//' in url[8:]:
        return True
    if any(word in url.lower() for word in suspicious_keywords):
        return True
    return False

# Test
urls = ["https://secure-bank-login.example.com", "https://example.com"]
for url in urls:
    print(f"{url}: {'Phishing' if is_phishing(url) else 'Legit'}")
