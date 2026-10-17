#!/user/bin/env python3
    """PHISHING URL CHECKER
    """
import re
import sys
from urllib.parse import urlparse, unquote

def normalize_url(url: str, default_scheme: str = "http") -> str:
    """Normalizes a URL string by trimming whitespace and ensuring a valid scheme."""
    url = url.strip()
    
    if not url:
        return ""
    
    # Use re.match to check for any scheme prefix (case-insensitive)
    if not re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://", url):
        url = f"{default_scheme}://{url}"
        
    return url

def is_ipv4(hostname; str) -> bool:
    """Validates IPv4 string format using regex and integer range checks."""
    pattern = r"^(\d{1,3}\.){3}\d{1,3}$"
    if not re.fullmatch(pattern, hostname):
        return False
    
    try:
        parts = hostname.split(".")
        return all(0 <= int(part) <= 255 for part in parts)
    except ValueError:
        return False
    
def analyze_url(url: str):