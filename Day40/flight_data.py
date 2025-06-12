class FlightData:
    """This class is responsible for structuring the flight data."""
    def __init__(self):
        pass

    def info_for_user(self, flight_info_6month):
        proposal = []
        for i in range(len(flight_info_6month)):
            for j in range(len(flight_info_6month[i])):
                # шлях
                road = [{"Departure at" : flight_info_6month[i][j]["itineraries"][0]["segments"][0]["departure"]["at"],}]

                # for k in range(len(flight_info_6month[i][j]["itineraries"][0]["segments"])):
                #
                #     body = {
                #         "Departure at" : flight_info_6month[i][j]["itineraries"][0]["segments"][k]["departure"]["at"],
                        # "From": flight_info_6month[i][j]["itineraries"][0]["segments"][k]["departure"]["iataCode"],
                        # "Arrival at" :flight_info_6month[i][j]["itineraries"][0]["segments"][k]["arrival"]["at"],
                        # "To": flight_info_6month[i][j]["itineraries"][0]["segments"][k]["arrival"]["iataCode"],
                    # }
                    # road.append(body)
                # price
                # price = flight_info_6month[i][j]["price"]["total"]
                # currency = flight_info_6month[i][j]["price"]["currency"]
                # duration =flight_info_6month[i][j]["itineraries"][0]["duration"],
                proposal.append( {
                    "road": road,
                    # "price": price,
                    # "currency": currency,
                    # "duration": duration,
                })
        print(proposal)
        return proposal
