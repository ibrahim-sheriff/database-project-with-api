import json

import requests

MAIN_URL = "http://127.0.0.1:8000"

response = requests.get(f"{MAIN_URL}/health")
print(response.content)

response = requests.get(f"{MAIN_URL}/students/4")
print(response.content)


new_student = {
    "id": 6,
    "first_name": "Mai",
    "last_name": "Samir",
    "phone": "019",
    "date_of_birth": "1999-11-11",
    "address": "Wonderland"
}
response = requests.post(f"{MAIN_URL}/students", data=json.dumps(new_student))
print(response.json())


update_student = {
    "id": 6,
    "first_name": "Mai",
    "last_name": "Samir",
    "phone": "0109",
    "date_of_birth": "1999-11-11",
    "address": "Wonderland"
}
response = requests.put(f"{MAIN_URL}/students/6", data=json.dumps(update_student))
print(response.json())
