import requests
import json
user_id = 2

url = f"https://reqres.in/api/users/{user_id}"

response = requests.get(url)
if response.status_code == 200:
    user_data = response.json().get("data", {})  # Extract user data
    formatted_response = {
        "data": {
            "id": user_data["id"],
            "email": user_data["email"],
            "first_name": user_data["first_name"],
            "last_name": user_data["last_name"],
            "avatar": user_data["avatar"]
        },
        "support": {
            "url": "https://reqres.in",
            "text": "NA"
        }
    }
    print(json.dumps(formatted_response, indent=4))
else:
    print(json.dumps({"error": f"Failed to retrieve user. Status code: {response.status_code}"}, indent=4))
