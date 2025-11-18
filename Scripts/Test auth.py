import requests
from requests.auth import HTTPBasicAuth

# Replace with your details
url = "https://infomedia.gipmbh.de/rest/api/space"
username = "chincholi"
password = ""   # only works if Basic Auth is enabled

response = requests.get(url, auth=HTTPBasicAuth(username, password))

if response.status_code == 200:
    print("Auth works! Spaces you can access:")
    for space in response.json().get("results", []):
        print(f"- {space['key']}: {space['name']}")
else:
    print(f" Failed: {response.status_code} {response.text}")
