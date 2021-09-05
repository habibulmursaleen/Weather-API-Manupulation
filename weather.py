import requests
import time

api = "https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=59.66554636551778&lon=9.68"
api_data = requests.get(api).json()

#print(api_data)

for item in api_data['properties']['timeseries']:
    temperature = item['data']['instant']['details']['air_temperature']
    description = item['data']['next_1_hours']['summary']['symbol_code']
    precipitation_amount = item['data']['next_1_hours']['details']['precipitation_amount']
    #humidity = item['data']['instant']['details']['relative_humidity']
    #wind_speed = item['data']['instant']['details']['wind_speed']

    print("Temperature: ", temperature)
    print("Description: ", description)
    print("Precipitation (mm) : ", precipitation_amount)
    #print("Humidity: ", humidity)
    #print("Wind Speed: ", wind_speed)
    print ("\n")