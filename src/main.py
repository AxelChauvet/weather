import requests


def call_api(route):
    url = f"https://api.weather.gov/{route}"
    response = requests.get(url)
    data = response.json()
    return data["features"]


for item in call_api("/stations?limit=5"):
    station_name = item["properties"]["name"]
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



