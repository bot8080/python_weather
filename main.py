# References
# https://realpython.com/python-gui-tkinter/
# https://openweathermap.org
# Stackoverflow


import tkinter as tk
from pyowm.utils import timestamps, formatting
from weatherManager import WeatherManager
from PIL import ImageTk, Image
import requests
import datetime

class weather_app:
    def __init__(self):
        self.window_height = 500
        self.window_width = 700
        self.window = tk.Tk()
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()
        self.window.resizable(False, False)
        self.window.title("Weather Application by Abhinav")
        self.api = 'be9ddc35227f67fba87decd2ea9e3d8f'

    def layout(self):
        center_x = int(self.screen_width/2 - self.window_width / 2)
        center_y = int(self.screen_height/2 - self.window_height / 2)

        self.window.geometry(f'{self.window_width}x{self.window_height}+{center_x}+{center_y}')
        
        self.window.configure(bg='#ADD8E6')
        
        city_frame = tk.Frame(self.window, bg='#ADD8E6')
        city_frame.pack(pady=20)
        
        city_label = tk.Label(city_frame, text="City Name", font=('calibri', 12), anchor='center', bg='#ADD8E6')
        city_label.pack(side=tk.LEFT, padx=10)
        
        self.city_entry = tk.Entry(city_frame)
        self.city_entry.pack(side=tk.LEFT)

        self.temp_label = tk.Label(self.window, text="Temperature: N/A", font=('calibri', 12), anchor='center', bg='#ADD8E6')
        self.temp_label.pack(pady=10)

        self.sunset_label = tk.Label(self.window, text="Sunset Time: N/A", font=('calibri', 12), anchor='center', bg='#ADD8E6')
        self.sunset_label.pack(pady=10)

        self.sunrise_label = tk.Label(self.window, text="Sunrise Time: N/A", font=('calibri', 12), anchor='center', bg='#ADD8E6')
        self.sunrise_label.pack(pady=10)

        self.wind_label = tk.Label(self.window, text="Wind Speed: N/A", font=('calibri', 12), anchor='center', bg='#ADD8E6')
        self.wind_label.pack(pady=10)

        self.humidity_label = tk.Label(self.window, text="Humidity: N/A", font=('calibri', 12), anchor='center', bg='#ADD8E6')
        self.humidity_label.pack(pady=10)

        self.pressure_label = tk.Label(self.window, text="Pressure: N/A", font=('calibri', 12), anchor='center', bg='#ADD8E6')
        self.pressure_label.pack(pady=10)

        self.detailed_status = tk.Label(self.window, text="Status: N/A", font=('calibri', 12), anchor='center', bg='#ADD8E6')
        self.detailed_status.pack(pady=10)

        self.icon_label = tk.Label(self.window, bg='#ADD8E6')
        self.icon_label.pack(pady=10)

        fetch_button = tk.Button(self.window, text="Fetch Data", command=self.fetch_data)
        fetch_button.pack(pady=20)

        # keep the window displaying
        self.window.mainloop()


    def fetch_data(self):
        city_name = self.city_entry.get()
        
        mgr = WeatherManager(self.api)
        
        data = mgr.get_weather_at_place(city_name)
        
        # Update the labels to display the weather data
        if data is not None:
            # Get the relevant data from the returned dictionary
            temp = data['temperature']
            sunset_time = datetime.datetime.fromtimestamp(data['sunset_time']).strftime('%I:%M %p')
            sunrise_time = datetime.datetime.fromtimestamp(data['sunrise_time']).strftime('%I:%M %p')
            wind = data['wind']
            humidity = data['humidity']
            pressure = data['pressure']
            status = data['status']
            detailed_status = data['detailed_status']
            weather_icon_url = data['weather_icon_url']

            # Load the weather icon
            # icon_image = Image.open(requests.get(weather_icon_url, stream=True).raw)
            # photo = ImageTk.PhotoImage(icon_image)

            # Update the labels
            self.temp_label.configure(text=f"Temperature: {temp} °F")
            self.sunset_label.configure(text=f"Sunset Time: {sunset_time}")
            self.sunrise_label.configure(text=f"Sunrise Time: {sunrise_time}")
            self.wind_label.configure(text=f"Wind Speed: {wind} mph")
            self.humidity_label.configure(text=f"Humidity: {humidity}%")
            self.pressure_label.configure(text=f"Pressure: {pressure} hPa")
            self.detailed_status.configure(text=f"Status: {detailed_status}")
            # self.icon_label.configure(image=photo)
            # self.icon_label.image = photo # keep a reference to avoid garbage collection


    def display_data(self):
        print(self.weather)
        print(self.main)
        print(self.wind)
        print(self.clouds)
        print(self.sys)

obj = weather_app()
obj.layout()
