import requests


def call_api(route):
    url = f"https://api.weather.gov/{route}"
    response = requests.get(url)
    data = response.json()
    return data["features"]


cities = {
    "1" : "Syracuse University",
    "2" : "Hillcrest Drive - San Luis Ibispo",
    "3" : "Golden Eagle",
    "4" : "Clayton Fire Co",
    "5" : "Eureka IDSM"
}
for item in cities:
    print(item, "-", cities[item])
choice = input("Choose a city: ")
city = cities[choice]
print(city)

for item in call_api("/stations?limit=500"):
    station_name = item["properties"]["name"]
    if station_name == city:
        station_identifier = item["properties"]["stationIdentifier"]
        for item in call_api(f"stations/{station_identifier}/observations"):
            station_temperature = item["properties"]["temperature"]["value"]
            station_wind = item["properties"]["windSpeed"]["value"]
            print(f"Station name: {station_name}")
            if station_temperature is None:
                print("Temperature: -")
            else:
                print(f"Temperature: {station_temperature}°C")
            if station_wind is None:
                print("Wind: -")
            else:
                print(f"Wind: {station_wind} km/h")
            print("##########################")
