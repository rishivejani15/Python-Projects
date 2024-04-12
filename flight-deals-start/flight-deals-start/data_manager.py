import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/d7def2c58f2007ddf01cb95a9f694db8/flightDeals/prices/[Object ID]"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.put(SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destiantion_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destiantion_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)