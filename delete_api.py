import requests
import json

api ="https://reqres.in/api"

authorization_token = "token token_value"

def del_req(user_id):
    url= api + "/users/{user_id}"
    headers = {"Authorization" : authorization_token}
    response= requests.delete(url, headers=headers)
    assert response.status_code==204
    print("The deleted user_id is",user_id)
    print("User deleted successfully")

del_req(1)

