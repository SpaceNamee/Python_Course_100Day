import flight_search, data_manager, flight_data, notification_manager
import json
import pprint
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
FLIGHT_API = "tO3ru6hpk9BCFtASVLY6dHyDne4SnBR0"
FLIGHT_SECRET_API = "uQbywGMDzo1EMHGj"

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
