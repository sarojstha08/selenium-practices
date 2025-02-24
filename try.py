import requests
import json

api = "https://reqres.in/api/users"

# Correcting the authorization header format
headers = {
    "Authorization": "Bearer your_token"  # Replace 'your_token' with the actual token
}

def get_request():
    url = api
    response = requests.get(url, headers=headers)  # Correct parameter passing

    # Checking if request was successful
    if response.status_code == 200:
        json_data = response.json()
        json_str = json.dumps(json_data, indent=4)
        print("The returned users for the API are:")
        print(json_str)
        print("-------------------")
    else:
        print(f"Request failed with status code: {response.status_code}")

get_request()
