import requests
from datetime import datetime

USERNAME = "marianna12345"
TOKEN = "k3nkj4n23jl43l2k342l43l3"
GRAPH_ID = "graph1"

# Create your user account
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token" : TOKEN ,
    "username": USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Create a graph definition
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_conf = {
    "id": GRAPH_ID,
    "name": "Life Graph",
    "unit": "commit",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_conf, headers=headers)
# print(response.text)

# Post value to the graph
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.today()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10"
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

# Update pixels

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_date = {
    "quantity": "1"
}

response = requests.put(url=update_endpoint, json=new_pixel_date, headers=headers)
print(response.text)