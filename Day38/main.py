import requests
from datetime import datetime
from os import getenv
from dotenv import load_dotenv
load_dotenv()

APP_ID = getenv("APP_ID")
API_KEY = getenv("API_KEY")

GENDER = "female"
WEIGHT_KG = "55"
HEIGHT_CM = "175"
AGE = "18"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
results = response.json()["exercises"]
#
header = {"Authorization":"Bearer marianna123456789qqq"}

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
SHEETY_ENDPOINT = "https://api.sheety.co/8d881c839880800babd48b988b035db5/myWorkouts/workouts"
for exercise in results:
    workouts = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(SHEETY_ENDPOINT, json=workouts, headers=header)

