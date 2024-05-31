import requests
from django.conf import settings


def get_nutrition_facts(ingredients):
    api_key = settings.CALORIES_NINJA_API_KEY
    url = "https://api.calorieninjas.com/v1/nutrition?query=" + ingredients
    headers = {
        "x-api-key": api_key
    }

    response = requests.get(url, headers=headers)  # Using GET instead of POST for this API

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error retrieving nutrition data: {response.status_code} {response.reason}")
        return None


