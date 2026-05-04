"""
Sample Application for CI Security Scanner (Secret Detection)
"""

import os
import hashlib

# ✅ Secure function
def secure_function(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

# ❌ Insecure examples (for demo)

# Hardcoded password (bad practice)
password = "admin123"

# Fake API key
api_key = "sk-1234567890abcdef"

# Fake token
token = "ghp_abcdef123456"

def run():
    print("Running secure function:", secure_function("my_secret_password"))
    print("Password:", password)
    print("API Key:", api_key)
    print("Token:", token)

if __name__ == "__main__":
    run()