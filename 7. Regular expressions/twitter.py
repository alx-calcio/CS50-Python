import re

url = input("URL: ").strip()

if matches := re.search(r".*twitter\.com/(\w+)", url, re.IGNORECASE):
    print(f"Username: {matches.group(1)}")
