import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get(
    f"https://itunes.apple.com/search?entity=song&limit=10&term={sys.argv[1]}"
)

o = response.json()  # o for object

print(json.dumps(o, indent=2))

for result in o["results"]:
    print(result["trackName"], end=",\n")
