#!/usr/bin/env python3
import sys
import requests
import re
import urllib.parse

def search_google(query):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    url = f"https://www.google.com/search?q={urllib.parse.quote(query)}"
    try:
        response = requests.get(url, headers=headers, timeout=10)
        # Look for the /url?q= pattern used in simple Google results
        links = re.findall(r'href="/url\?q=(https?://[^&]+)', response.text)
        if not links:
            # Fallback to direct https links
            links = re.findall(r'href="(https?://[^"]+)"', response.text)
            
        external_links = []
        seen = set()
        for l in links:
            l = urllib.parse.unquote(l)
            if any(x in l for x in ["google.com", "gstatic.com", "w3.org", "schema.org", "youtube.com"]):
                continue
            if l not in seen:
                external_links.append(l)
                seen.add(l)
        return external_links[:10]
    except Exception as e:
        return [f"Exception: {str(e)}"]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: free_search.py <query>")
        sys.exit(1)
    
    query = sys.argv[1]
    results = search_google(query)
    for i, link in enumerate(results, 1):
        print(f"{i}. {link}")
