from pyowm import OWM

class WeatherManager:
    def __init__(self, api_key):
        self.owm = OWM(api_key)
        self.mgr = self.owm.weather_manager()
    
    def get_weather_at_place(self, place):
        observation = self.mgr.weather_at_place(place)
        weather_dict = observation.weather.to_dict()
        weather_dict["weather_icon_url"] = observation.weather.weather_icon_url
        return [observation.weather, weather_dict]
        # print(observation.weather.temperature('fahrenheit'))
        # print(observation.weather.temperature('celsius'))
        # print(weather_dict)
        # return  weather_dict
    
    def print_weather_details(self, weather):
        # print("\nBarometric pressure:", weather.barometric_pressure)
        # print("\nClouds:", weather.clouds)
        # print("\nDetailed status:", weather.detailed_status)
        # print("\nDew point:", weather.dewpoint)
        # print("\nHeat index:", weather.heat_index)
        # print("\nHumidex:", weather.humidex)
        # print("\nHumidity:", weather.humidity)
        # print("\nPrecipitation probability:", weather.precipitation_probability)
        # print("\nPressure:", weather.pressure)
        # print("\nRain:", weather.rain)
        # print("\nReference time:", weather.ref_time)
        # print("\nStatus:", weather.status)
        # print("\nSnow:", weather.snow)
        # print("\nSunrise time:", weather.srise_time)
        # print("\nSunset time:", weather.sset_time)
        # print("\nTemperature:", weather.temperature('fahrenheit'))
        # print("\nTo dict:", weather.to_dict())
        # print("\nUTC offset:", weather.utc_offset)
        # print("\nUV index:", weather.uvi)
        # print("\nVisibility:", weather.visibility())
        # print("\nVisibility distance:", weather.visibility_distance)
        # print("\nWeather code:", weather.weather_code)
        # print("\nWeather icon name:", weather.weather_icon_name)
        # print("\nWeather icon URL:", weather.weather_icon_url)
        # print("\nWind:", weather.wind())

        return  weather.to_dict()
