import requests
import json

api = "https://reqres.in/api"
authorization_token = "token token_value"

def put_req(user_id):
    # Use the user_id to construct the URL correctly
    url = "{api}/users/{user_id}"
    headers = {
        "Authorization": authorization_token,
        "Content-Type": "application/json"
    }
    data = {
        "name": "John",
        "job": "QA tester"
    }
    
    response = requests.put(url, json=data, headers=headers)
    if response.status_code == 200:
        json_data = response.json()
        json_str = json.dumps(json_data, indent=4)
        print("The updated user is:")
        print(json_str)
        print("-----------------------------------")
    else:
        print("Failed to update user. Status Code:", response.status_code)
        print("Response:", response.text)
put_req(1)
