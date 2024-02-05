import os
from datetime import datetime

import requests

nutritionix_id = os.environ["NUTRITIONIX_ID"]
nutritionix_key = os.environ["NUTRITIONIX_KEY"]
nutritionix_endpoint = os.environ["NUTRITIONIX_ENDPOINT"]

nutritionix_header = {
    "x-app-id": nutritionix_id,
    "x-app-key": nutritionix_key,
}

query = input("Tell me which exercises you did: ")

user_params = {
    "query": query
}

response = requests.post(url=nutritionix_endpoint, data=user_params, headers=nutritionix_header)
workouts = response.json()["exercises"]

sheety_token = os.environ["SHEETY_TOKEN"]
sheety_endpoint = os.environ["SHEETY_ENDPOINT"]
sheety_header = {
    "Authorization": f"Bearer {sheety_token}",
}

date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")

for workout in workouts:
    user_params = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": workout["name"].title(),
            "duration": workout["duration_min"],
            "calories": workout["nf_calories"],
        }
    }

    response = requests.post(url=sheety_endpoint, json=user_params, headers=sheety_header)
    print(response.json())