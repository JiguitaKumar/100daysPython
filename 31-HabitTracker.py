import requests
from datetime import datetime

USERNAME = "some_username"
TOKEN = "some_token"
GRAPH_NAME = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": GRAPH_NAME,
    "name": "Steps Tracker",
    "unit": "Steps",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

post_endpoint = f"{graph_endpoint}/{GRAPH_NAME}"

today = datetime.now()

post_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "5479"
}

# response = requests.post(url=post_endpoint, json=post_params, headers=headers)
# print(response.text)

put_endpoint = f"{post_endpoint}/20251129"

put_params = {
    "quantity": "199"
}

# response = requests.put(url=put_endpoint, json=put_params, headers=headers)
# print(response.text)

delete_endpoint = f"{post_endpoint}/20251201"

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
