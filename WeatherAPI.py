import json
import requests
from operator import itemgetter

class WeatherAPI:
    def __init__(self, city):
        with open('api.json') as f:
            api = json.load(f)
        self.api_key = api['api']
        self.city = city
        self.state = ''
        self.country = ''

    def get_coordinates(self):
        url = f"http://api.openweathermap.org/geo/1.0/direct?q={self.city},{self.state},{self.country}&limit=5&appid={self.api_key}"
        # print(url)
        response = requests.get(url)
        response.raise_for_status()
        json_object = json.loads(response.text)
        counter = 0 
        dictionary = {}
        for location in json_object:
            lat, lon, country = itemgetter("lat", "lon", "country")(json_object[counter])
            dictionary[country] = [lat, lon]
            counter = counter+1
        print(dictionary)
        return dictionary        

    def get_weather_data(self, lat, lon):
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={self.api_key}"
        # print(url)
        response = requests.get(url)
        response.raise_for_status()
        json_object = json.loads(response.text) 
        weather, main, wind, clouds, sys = itemgetter("weather", "main","wind", "clouds", "sys")(json_object)
        return weather, main, wind, clouds, sys
    
    def get_location(self):
        dictionary = self.get_coordinates()
        for key in dictionary.keys():
            # print(key, val)
            data = self.get_weather_data(dictionary[key][0], dictionary[key][1])

        for d in data:
            print(d)
        

