import requests
import json

class DataManager:
    """This class is responsible for talking to the Google Sheet."""

    def __init__(self, func):
        self.get_url = "https://api.sheety.co/faf6982077377efcd40a30fa60babe18/flight/prices"
        self.dict_city = self.update_data(func)

    def update_data(self, func):
        response = requests.get(url=self.get_url)
        loads_data = response.json().get("prices")
        dict_city_code = {}
        for i in range(len(loads_data)):
            city = loads_data[i]["city"]
            iata_code = func(city)

            loads_data[i]["iataCode"] = iata_code
            price = loads_data[i]["lowestPrice"]
            dict_city_code[city] = {"iata_code":iata_code, "price":price}
            body = {
                "price": loads_data[i]
            }
            response = requests.put(url=f"https://api.sheety.co/faf6982077377efcd40a30fa60babe18/flight/prices/{i + 2}",
                                    json=body)


        with open("data.json", "w") as file:
            json.dump(loads_data, file, indent=4)

        return dict_city_code
