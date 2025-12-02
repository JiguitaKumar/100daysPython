import requests
from datetime import datetime
import os

APP_ID = os.environ.get("MY_APP_ID")
APP_KEY = os.environ.get("MY_APP_KEY")

nutrition_base_url = "https://app.100daysofpython.dev"

args = {
    "query": input("Tell me which exercises you did: "),
    "weight_kg": 70,
    "heigth_cm": 175,
    "age": 30,
    "gender": "male"
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

response = requests.post(url=f"{nutrition_base_url}/v1/nutrition/natural/exercise", json=args, headers=headers)
response.raise_for_status()
print(response.status_code)
data = response.json()

sheet_api_url = os.environ.get("MY_SHEET_API_URL")

date_now = datetime.now()

exercise_params = {
    "exercise": {
        "Date": date_now.strftime("%d/%m/%Y"),
        "Time": date_now.strftime("%H:%M:%S"),
        "Exercise": data['exercises'][0]['name'].title(),
        "Duration": data['exercises'][0]['duration_min'],
        "Calories": data['exercises'][0]['nf_calories']
    }
}

sheet_headers = {
    "Authorization": f"Basic {os.environ.get("MY_SHEET_TOKEN")}"
}

sheet_response = requests.post(url=sheet_api_url, json=exercise_params, headers=sheet_headers)
print(sheet_response.text)

