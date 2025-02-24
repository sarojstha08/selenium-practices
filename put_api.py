import requests
import json

api= "https://reqres.in/api"

authorization_token= "token token_value"

def put_req(user_id):
    url = api + "/users/"
    headers = {"Authorization": authorization_token}
    data = {
            "name": "John",
            "job": "QA tester"
        }
       
    response = requests.put(url, json=data, headers=headers)
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    assert response.status_code==200
    print("The updated user is:",json_str)
    print("-----------------------------------")
    

put_req(1)



