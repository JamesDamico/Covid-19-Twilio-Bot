import requests
import os
from dotenv import load_dotenv

load_dotenv()

url = "https://api.covidactnow.org/v2/state/NY.json" # API URL

def _call_api():

    # API Call
    res = requests.get(
        url,
        headers={"Accept": "application/json"},
        params={
            "apiKey": os.getenv("COVID_API")
        }
    )

    data = res.json() # Store the JSON in a variable

    return data


def get_data():

    data = _call_api()

    # Extract Data from JSON
    new_cases = data["actuals"]["newCases"]
    new_deaths = data["actuals"]["newDeaths"]
    population_with_first_dose = round(float(data["metrics"]["vaccinationsInitiatedRatio"]) * 100, 2)
    population_fully_vaccinated = round(float(data["metrics"]["vaccinationsCompletedRatio"]) * 100, 2)

    return [new_cases, new_deaths, population_with_first_dose, population_fully_vaccinated]