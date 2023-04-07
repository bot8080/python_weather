import tkinter as tk
import requests
from weatherManager import WeatherManager 
import time
import datetime
from PIL import Image, ImageTk
import yaml


class WeatherApp:
    def __init__(self, window):
        self.flag = 0
        self.temp = 0
        self.window = window
        self.window.title("Weather App BY Abhinav Khanna")
        self.window.config(bg='#DADAA5')
        self.window.geometry("1920x1080")
        self.api = 'be9ddc35227f67fba87decd2ea9e3d8f'
        
        self.clock = tk.Label(self.window, font=("Calibri", 20), bg="#DADAA5", fg="white")
        self.clock.place(x=500, y=50, height=50, width=300)
        
        self.weather_counter = tk.Label(self.window, font=("Calibri", 20), bg='#DADAA5', fg='white')
        self.weather_counter.place(x=1000, y=50, height=50, width=400)

        with open('config.yml', 'r') as f:
            self.config = yaml.safe_load(f)

        self.city = self.config['city']
        self.counter = self.config['fetch_interval']
    
    def layout(self):
        tk.Label(self.window, text="Check Weather", font=("calibri", 30, "bold"), bg='#DADAA5', fg='white').place(x=100, y=50, height=50, width=350)
        
        # city_name = StringVar()

        self.city_entry = tk.Entry(self.window, font=("calibri", 20, "bold"))
        self.city_entry.place(x=100, y=150, height=30, width=200)
        tk.Button(self.window, text="Fetch Data", command=self.fetch_data).place(x=320, y=150, height=30, width=150)

        # Left Layout
        self.temp_label = tk.Label(self.window, text="", font=("calibri", 10, "bold"), anchor="center")
        self.temp_label.place(x=200, y=260, height=30, width=200)

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

    def fetch_data(self):
        self.city = self.config['city']
        self.counter = self.config['fetch_interval']
        try:
            self.city = self.city_entry.get()
            if self.city == "":
                self.city = self.config['city']
            # print("TRY")
            # print(self.city)
        except Exception as e:
            print("EXCEPTION ",self.city)
            print(e)
        
        # print("HERE")
        mgr = WeatherManager(self.api)
        data = mgr.get_weather_at_place(self.city)

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
            status = data[1]['status']
            detailed_status = data[1]['detailed_status']

            self.currtemp.config(text=f"{self.kelvin_to_celsius(temp)} | {self.kelvin_to_fahrenheit(temp)}")
            self.mintemp.config(text=f"{self.kelvin_to_celsius(min_temp)} | {self.kelvin_to_fahrenheit(min_temp)}")
            self.maxtemp.config(text=f"{self.kelvin_to_celsius(max_temp)} | {self.kelvin_to_fahrenheit(max_temp)}")
            self.feelslike.config(text=f"{self.kelvin_to_celsius(feels_like)} | {self.kelvin_to_fahrenheit(feels_like)}")
            self.sunrise.config(text=f"{sunrise_time}")
            self.sunset.config(text=f"{sunset_time}")
            self.windspeed.config(text=f"{wind} mph")
            self.pressure.config(text=f"{pressure} hPa")
            self.status.config(text=f"{detailed_status}")
            self.temp_label.config(text = f"Today's {self.city} Temperature")
            self.place_image(status)

    def get_time(self):
        timeVar= time.strftime("%I:%M:%S %p")
        self.clock.config(text=str(datetime.datetime.now().date())+" | "+ timeVar)
        self.clock.after(1000,self.get_time)

    def update_weather(self):
        self.counter = self.counter -1
        if self.counter==0:
            self.counter = self.config['fetch_interval']
            self.fetch_data()
            self.weather_counter.after(1000, self.update_weather)
        else :
            self.weather_counter.config(text="Next Update in : " + str(self.counter))
            self.weather_counter.after(1000, self.update_weather)

    def kelvin_to_celsius(self, kelvin):
        celsius = kelvin - 273.15
        return str(round(celsius, 2)) + " °C"
    
    def kelvin_to_fahrenheit(self, kelvin):
        fahrenheit = (kelvin - 273.15) * 9/5 + 32
        return str(round(fahrenheit,2)) + " °F"
    
    def place_image(self,Weather_status):
        # print(Weather_status)
        if Weather_status == "Clear":
            img = Image.open("images/day_clear_sky.png")
            resized_img = img.resize((100, 100))
            tk_img = ImageTk.PhotoImage(resized_img)
            label = tk.Label(image=tk_img, bg="black")
            label.image = tk_img 
            label.place(x=1100, y=230)
        elif Weather_status == "Clouds":
            img = Image.open("images/broken_clouds.png")
            resized_img = img.resize((100, 100))
            tk_img = ImageTk.PhotoImage(resized_img)
            label = tk.Label(image=tk_img, bg="black")
            label.image = tk_img 
            label.place(x=1100, y=230)
        elif Weather_status == "Mist":
            img = Image.open("images/mist.png")
            resized_img = img.resize((100, 100))
            tk_img = ImageTk.PhotoImage(resized_img)
            label = tk.Label(image=tk_img, bg="black")
            label.image = tk_img 
            label.place(x=1100, y=230)
        elif Weather_status == "Rain":
            img = Image.open("images/rain.png")
            resized_img = img.resize((100, 100))
            tk_img = ImageTk.PhotoImage(resized_img)
            label = tk.Label(image=tk_img, bg="black")
            label.image = tk_img 
            label.place(x=1100, y=230)
        elif Weather_status == "Haze":
            img = Image.open("images/day_few_clouds.png")
            resized_img = img.resize((100, 100))
            tk_img = ImageTk.PhotoImage(resized_img)
            label = tk.Label(image=tk_img, bg="black")
            label.image = tk_img 
            label.place(x=1100, y=230)
        elif Weather_status == "Snow":
            img = Image.open("images/snow.png")
            resized_img = img.resize((100, 100))
            tk_img = ImageTk.PhotoImage(resized_img)
            label = tk.Label(image=tk_img, bg="black")
            label.image = tk_img 
            label.place(x=1100, y=230)
        else:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    obj = WeatherApp(root)
    obj.layout()
    obj.get_time()
    root.after(1000, obj.fetch_data())
    root.after(1000, obj.update_weather())
    root.mainloop()

