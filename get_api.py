import requests
import json

api = "https://reqres.in/api/users"

authorization = "token = any_token"

def get_request():
    url = api
    headers= authorization
    response = requests.get(url)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("The returned users for the api are:",json_str)
    print("-------------------")

get_request()