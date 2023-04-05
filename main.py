import tkinter as tk
import requests
from weatherManager import WeatherManager 
import time
import datetime

class WeatherApp:
    def __init__(self, window):
        self.counter = 10
        self.city_list = []
        self.flag = 0
        self.temp = 0
        self.window = window
        self.window.title("Weather App BY Abhinav Khanna")
        self.window.config(bg='#DADAA5')
        self.window.geometry("1920x1080")
        self.api = 'be9ddc35227f67fba87decd2ea9e3d8f'
        
        self.clock = tk.Label(self.window, font=("Calibri", 40), bg="#DADAA5", fg="white")
        self.clock.place(x=500, y=50, height=50, width=350)
        
        self.l1_WeatherUp = tk.Label(self.window, font=("Calibri", 40), bg='#DADAA5', fg='white')
        self.l1_WeatherUp.place(x=520, y=450, height=100, width=540)
    
    def layout(self):
        name_label = tk.Label(self.window, text="Check Weather", font=("calibri", 30, "bold"), bg='#DADAA5', fg='white').place(x=100, y=50, height=50, width=350)
        
        # city_name = StringVar()

        self.city_entry = tk.Entry(self.window, font=("calibri", 20, "bold"))
        self.city_entry.place(x=100, y=150, height=30, width=200)
        fetch_data = tk.Button(self.window, text="Fetch Data", command=self.fetch_data).place(x=320, y=150, height=30, width=150)

        # Left Layout
        tk.Label(self.window, text="Temperature Details", font=("calibri", 10, "bold"), anchor="center").place(x=200, y=260, height=30, width=200)

        tk.Label(self.window, text="Current Temperature", font=("calibri", 10, "bold"), anchor="w", bg='#DADAA5').place(x=100, y=300, height=30, width=180)
        self.currtemp = tk.Label(self.window, text="", font=("calibri", 10))
        self.currtemp.place(x=320, y=300, height=30, width=150)

        tk.Label(self.window, text="Min Temperature", font=("calibri", 10, "bold"), anchor="w", bg='#DADAA5').place(x=100, y=340, height=30, width=180)
        self.mintemp = tk.Label(self.window, text="", font=("calibri", 10))
        self.mintemp.place(x=320, y=340, height=30, width=150)

        tk.Label(self.window, text="Max Temperature", font=("calibri", 10, "bold"), anchor="w", bg='#DADAA5').place(x=100, y=380, height=30, width=180)
        self.maxtemp = tk.Label(self.window, text="", font=("calibri", 10))
        self.maxtemp.place(x=320, y=380, height=30, width=150)


        # Right Layout

        tk.Label(self.window, text="Other Details", font=("calibri", 10, "bold"), anchor="center").place(x=650, y=150, height=30, width=200)

        tk.Label(self.window, text="Feels Like", font=("calibri", 10, "bold"), anchor="w", bg='#DADAA5').place(x=600, y=190, height=30, width=150)
        self.feelslike = tk.Label(self.window, text="", font=("calibri", 10))
        self.feelslike.place(x=800, y=190, height=30, width=150)

        tk.Label(self.window, text="Sunrise Time", font=("calibri", 10, "bold"), anchor="w", bg='#DADAA5').place(x=600, y=230, height=30, width=150)
        self.sunrise = tk.Label(self.window, text="", font=("calibri", 10))
        self.sunrise.place(x=800, y=230, height=30, width=150)

        tk.Label(self.window, text="Sunset Time", font=("calibri", 10, "bold"), anchor="w", bg='#DADAA5').place(x=600, y=270, height=30, width=150)
        self.sunset = tk.Label(self.window, text="", font=("calibri", 10))
        self.sunset.place(x=800, y=270, height=30, width=150)

        tk.Label(self.window, text="Windspeed", font=("calibri", 10, "bold"), anchor="w", bg='#DADAA5').place(x=600, y=310, height=30, width=150)
        self.windspeed = tk.Label(self.window, text="", font=("calibri", 10))
        self.windspeed.place(x=800, y=310, height=30, width=150)
        
        tk.Label(self.window, text="Pressure", font=("calibri", 10, "bold"), anchor="w", bg='#DADAA5').place(x=600, y=350, height=30, width=150)
        self.pressure = tk.Label(self.window, text="", font=("calibri", 10))
        self.pressure.place(x=800, y=350, height=30, width=150)

        tk.Label(self.window, text="Weather Status", font=("calibri", 10, "bold"), anchor="w", bg='#DADAA5').place(x=600, y=390, height=30, width=150)
        self.status = tk.Label(self.window, text="", font=("calibri", 10))
        self.status.place(x=800, y=390, height=30, width=150)

    def fetch_data(self, city_name="Sarnia"):
        try:
            city_name = self.city_entry.get()
            print(city_name)
        except Exception as e:
            print("EXCEPTION ",city_name)
            print(e)
        
        # print(city_name)
        mgr = WeatherManager(self.api)
        data = mgr.get_weather_at_place(city_name)

        # Update the labels to display the weather data
        if data is not None:
            # Get the relevant data from the returned dictionary
            temp = data[1]['temperature']['temp']
            # temp_cel = data[0].temperature('celsius')
            max_temp = data[1]['temperature']['temp_max']
            min_temp = data[1]['temperature']['temp_min']
            feels_like = data[1]['temperature']['feels_like']
            sunrise_time = datetime.datetime.fromtimestamp(data[1]['sunrise_time']).strftime('%I:%M %p')
            sunset_time = datetime.datetime.fromtimestamp(data[1]['sunset_time']).strftime('%I:%M %p')
            wind = data[1]['wind']['speed']
            humidity = data[1]['humidity']
            pressure = data[1]['pressure']['press']
            detailed_status = data[1]['detailed_status']

            self.currtemp.config(text=f"{self.kelvin_to_celsius(temp)} | {self.kelvin_to_fahrenheit(temp)}")
            self.mintemp.config(text=f"{self.kelvin_to_celsius(min_temp)} | {self.kelvin_to_fahrenheit(min_temp)}")
            self.maxtemp.config(text=f"{self.kelvin_to_celsius(max_temp)} | {self.kelvin_to_fahrenheit(max_temp)}")
            self.feelslike.config(text=f"{self.kelvin_to_celsius(feels_like)} | {self.kelvin_to_fahrenheit(feels_like)}")
            self.sunrise.config(text=f"{sunrise_time}")
            self.sunset.config(text=f"{sunset_time}")
            self.windspeed.config(text=f"{wind} mph")
            # self.labels[7].config(text=f": {humidity}%")
            self.pressure.config(text=f"{pressure} hPa")
            self.status.config(text=f"{detailed_status}")
            self.update_weather()


    def get_time(self):
        timeVar= time.strftime("%I:%M:%S %p")
        self.clock.config(text=timeVar)
        self.clock.after(1000,self.get_time)

        
    def update_weather(self):
        self.counter = self.counter -1
        if self.counter<0:
            self.get_data()
        else :
            self.l1_WeatherUp.config(text="Updating Weather in : " + str(self.counter))
            self.l1_WeatherUp.after(1000, self.update_weather)

    def kelvin_to_celsius(self, kelvin):
        celsius = kelvin - 273.15
        return str(round(celsius, 2)) + " °C"
    
    def kelvin_to_fahrenheit(self, kelvin):
        fahrenheit = (kelvin - 273.15) * 9/5 + 32
        return str(round(fahrenheit,2)) + " °F"

if __name__ == "__main__":
    root = tk.Tk()
    obj = WeatherApp(root)
    obj.layout()
    obj.get_time()
    root.mainloop()

