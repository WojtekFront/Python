import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "helloworld")

if response.status_code == 200:
    answear = requests.post(BASE + "helloworld")

print(response.json())