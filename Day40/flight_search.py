import json
from datetime import datetime, timedelta
import requests

class FlightSearch:
    """This class is responsible for talking to the Flight Search API."""

    def __init__(self, api, secret_api):
        self.api_key = api
        self.secret_api_key = secret_api
        self.token = self.get_token()

    def get_token(self):
        url = "https://test.api.amadeus.com/v1/security/oauth2/token"

        data = {
            "grant_type": "client_credentials",
            "client_id": self.api_key,
            "client_secret": self.secret_api_key
        }

        response = requests.post(url, data = data)
        token  = response.json().get("access_token")
        if response.status_code == 200:
            return token
        else:
            return None


    def make_flight_search(self, destination, max_price, adults="1", origin="JFK"):
        url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        response = []
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        for i in range(2):
            current_date = datetime.today() + timedelta(i+1)
            params = {
                "originLocationCode": origin,
                "destinationLocationCode": destination,
                "departureDate": current_date.strftime("%Y-%m-%d"),
                # "nonStop": "True",
                "adults": adults,
                "maxPrice": max_price,
            }

            res = requests.get(url, headers=headers, params=params)
            print(res.status_code)
            print(res.text)
            if (res.json()["data"] != []):
                response.append(res.json()["data"])

        return response

    def code_search(self, city):
        url = "https://test.api.amadeus.com/v1/reference-data/locations/cities"

        params = {
            "keyword": city,
        }

        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(url, params=params, headers=headers)

        return response.json()["data"][0]["iataCode"]

