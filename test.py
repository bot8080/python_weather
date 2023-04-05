import tkinter as tk
import tkinter.font as tkFont
from pyowm.utils import timestamps, formatting
from weatherManager import WeatherManager
from PIL import ImageTk, Image
import requests
import datetime
import pytz
import time
from tkinter import PhotoImage

class weather_app:
    def __init__(self, root):
        self.window_height = 500
        self.window_width = 800
        self.window = root
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()
        self.window.resizable(False, False)
        self.window.title("Weather Application by Abhinav")
        self.api = 'be9ddc35227f67fba87decd2ea9e3d8f'
        self.image_icon = PhotoImage(file="./images/weather.png")
        self.window.iconphoto(False, self.image_icon)

        # self.canvas = tk.Canvas(root, width=300, height=200)
        # self.canvas.pack()
        # self.image = ImageTk.PhotoImage(file="./images/background.png")
        # self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)
    
    def layout(self):
        center_x = int(self.screen_width/2 - self.window_width / 2)
        center_y = int(self.screen_height/2 - self.window_height / 2)

        self.window.geometry(f'{self.window_width}x{self.window_height}+{center_x}+{center_y}')

        self.window.configure(bg='#B3B3EE')

        self.current_time_label = tk.Label(self.window, text="Current Time",font=("Arial", 10, "bold"), fg="#333333", bg="#B3B3EE", justify="left" ).place(x=0,y=70,width=140,height=30)

        self.counter_label = tk.Label(self.window, text="Counter" ,font=("Arial", 10, "bold"), fg="#333333", bg="#B3B3EE", justify="left").place(x=170,y=70,width=70,height=25) 

        self.city_label = tk.Label(self.window, text="City Name", font=("Arial", 10, "bold"), fg="#333333", bg="#B3B3EE", justify="left").place(x=20, y=140, width=80, height=25)
        
        try:
            self.city_entry = tk.Entry(self.window, font=("Arial", 10), fg="#8c3434", justify="left", relief="sunken")
            self.city_entry.place(x=100, y=140, width=89, height=25)
        except Exception as E:
            print(E)       

        self.fetch_button = tk.Button(self.window, text="Fetch Data", font=("Arial", 10), bg="#2986cc", fg="white",
                                 activebackground="#2e4691", activeforeground="#393d49", command=self.fetch_data).place(x=50, y=180, width=80, height=25)

        tk.Label(self.window, text = f"Other Details {self.city_entry}", font=("Arial", 10), fg="#8c3434", justify="left").place(x=310, y=140, width=126, height=30)
       
        # details_frame = tk.Frame(self.window, bg="#DADAA5")
        # details_frame.place(x=310, y=130, width=200, height=500)

        # details_heading = tk.Label(details_frame, text="Other Details", font=("Arial", 10), fg="black", bg="#DADAA5")
        # details_heading.pack(side="top", fill="x", pady=5)

        label1_data = {
            "Temperature Details":      {"x": 40, "y": 250, "width": 147},
            "Temperature":              {"x": 30, "y": 290, "width": 108},
            "val_Temp":                 {"x": 150,"y": 290, "width": 70},
            "Min Temperature":          {"x": 30, "y": 320, "width": 108},
            "val_min_temp":             {"x": 150,"y": 320, "width": 70},
            "Max Temperature":          {"x": 30, "y": 350, "width": 108},
            "val_max_temp":             {"x": 150, "y": 350, "width": 70}
        }

        for label, data in label1_data.items():
            label_var = tk.Label(self.window, text=label, font=('Arial', 10), fg="#333333", anchor='w', bg='#B3B3EE')
            label_var.place(x=data["x"], y=data["y"], width=data["width"], height=30)

        label2_data = {
            "Feels Like":               {"x": 290, "y": 160, "width": 112},
            "val_feels_like":           {"x": 420, "y": 160, "width": 112},
            "Sunrise Time":             {"x": 290, "y": 190, "width": 112},
            "val_sunrise":              {"x": 420, "y": 190, "width": 112},
            "Sunset Time":              {"x": 290, "y": 220, "width": 112},
            "val_sunset":               {"x": 420, "y": 220, "width": 112},
            "Wind Speed":               {"x": 290, "y": 250, "width": 112},
            "val_wind":                 {"x": 420, "y": 250, "width": 112},
            "Humidity":                 {"x": 290, "y": 280, "width": 112},
            "val_humidity":             {"x": 420, "y": 280, "width": 112},
            "Pressure":                 {"x": 290, "y": 310, "width": 112},
            "val_pressure":             {"x": 420, "y": 310, "width": 112},
            "Status":                   {"x": 290, "y": 340, "width": 112},
            "val_status":               {"x": 420, "y": 340, "width": 112}
        }

        self.labels = []
        for label, data in label2_data.items():
            label_var = tk.Label(self.window, text=label, font=('Arial', 10), fg="#333333", anchor='w', bg='#B3B3EE')
            label_var.place(x=data["x"], y=data["y"], width=data["width"], height=30)
            self.labels.append(label_var)


            if label.startswith("val_"):
                self.labels.append(label_var)

        print(self.labels)


    def fetch_data(self, city_name=""):
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

            self.labels[0].configure(text=f"Temperature: {self.kelvin_to_celsius(temp)}")
            self.labels[1].configure(text=f"Min Temperature: {self.kelvin_to_celsius(min_temp)}")
            self.labels[2].configure(text=f"Max Temperature: {self.kelvin_to_celsius(max_temp)}")
            self.labels[3].configure(text=f"Feels Like: {self.kelvin_to_celsius(feels_like)}")
            self.labels[4].configure(text=f"Sunrise Time: {sunrise_time}")
            self.labels[5].configure(text=f"Sunset Time: {sunset_time}")
            self.labels[6].configure(text=f"Wind Speed: {wind} mph")
            self.labels[7].configure(text=f"Humidity: {humidity}%")
            self.labels[8].configure(text=f"Pressure: {pressure} hPa")
            self.labels[9].configure(text=f"Status: {detailed_status}")
    
    def update_clock(self):
        current_time = time.strftime('%H:%M:%S')
        self.clock_label.configure(text=current_time)
        self.date_label.configure(text=time.strftime('Today is %A, %B %d, %Y'))
        self.after(1000, self.update_clock)

    def kelvin_to_celsius(self, kelvin):
        celsius = kelvin - 273.15
        return str(round(celsius, 2)) + " °C"
    
    def kelvin_to_fahrenheit(self, kelvin):
        fahrenheit = (kelvin - 273.15) * 9/5 + 32
        return str(round(fahrenheit,2)) + " °F"
    
if __name__ == "__main__":
    root = tk.Tk()
    app = weather_app(root)
    app.layout()
    # app.fetch_data("sarnia")
    root.mainloop()
