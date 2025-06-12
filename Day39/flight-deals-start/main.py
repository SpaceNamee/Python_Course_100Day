import flight_search, data_manager, flight_data, notification_manager
import json
import pprint
from os import getenv
from dotenv import load_dotenv
load_dotenv()
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
FLIGHT_API = getenv("FLIGHT_API")
FLIGHT_SECRET_API = getenv("FLIGHT_SECRET_API")

searcher = flight_search.FlightSearch(FLIGHT_API,FLIGHT_SECRET_API)
active_data = data_manager.DataManager(searcher.code_search)
maker_user_info = flight_data.FlightData()
sender = notification_manager.NotificationManager()

city_code_data = active_data.dict_city
for i in city_code_data:
    data = searcher.make_flight_search(city_code_data[i]["iata_code"] ,city_code_data[i]["price"] )
    if len(data) != 0:
        data_for_user = maker_user_info.info_for_user(data)
        sender.send_info(destination=i, info=data_for_user)
# data = ex.make_flight_search("LON", 250)
# nono = flight_data.FlightData(data)
# nono.info_for_user()
# pprint.pprint()
# ex.code_search("Paris")
# data_manager = data_manager.DataManager(ex.code_search)
# data_manager.make()
