import requests
import json
url = "https://reqres.in/api/users"

payload = {
    "name": "Ricky Ponting",
    "job": "Right hand Batsman"
}
response = requests.post(url, json=payload)

if response.status_code == 201:
    created_user = response.json()
    print(json.dumps(created_user, indent=4))
else:
    print(json.dumps({"error": f"Failed to create user. Status code: {response.status_code}"}, indent=4))