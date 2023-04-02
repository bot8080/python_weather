# References
# https://realpython.com/python-gui-tkinter/
# https://openweathermap.org
# Stackoverflow


import tkinter as tk
from WeatherAPI import WeatherAPI

class weather_app:
    def __init__(self):
        self.window_height = 400
        self.window_width = 500
        self.window = tk.Tk()
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()
        self.window.resizable(False, False)
        self.window.title("Weather Application by Abhinav")

    def layout(self):
        center_x = int(self.screen_width/2 - self.window_width / 2)
        center_y = int(self.screen_height/2 - self.window_height / 2)

        self.window.geometry(f'{self.window_width}x{self.window_height}+{center_x}+{center_y}')
        
        city_label = tk.Label(self.window, text="City Name", font=('calibri', 12))
        city_label.grid(row=0, column=0)
        self.city_entry = tk.Entry(self.window)
        self.city_entry.grid(row=0, column=1)

        # state_label = tk.Label(self.window, text="State", font=('calibri', 12))
        # state_label.grid(row=1, column=0)
        # self.state_entry = tk.Entry(self.window)
        # self.state_entry.grid(row=1, column=1)

        temp_label = tk.Label(self.window, text="Temperature", font=('calibri', 12))
        temp_label.grid(row=2, column=0)

        desc_label = tk.Label(self.window, text="Description", font=('calibri', 12))
        desc_label.grid(row=3, column=0)

        icon_label = tk.Label(self.window, text="Icon")
        icon_label.grid(row=4, column=0)

        wind_label = tk.Label(self.window, text="Wind Speed", font=('calibri', 12))
        wind_label.grid(row=5, column=0)

        fetch_button = tk.Button(self.window, text="Fetch Data", command=self.fetch_data)
        fetch_button.grid(row=6, column=1)

        # keep the window displaying
        self.window.mainloop()

    def fetch_data(self):
        city = self.city_entry.get()
        # state = self.state_entry.get()
        # country = self.country_entry.get()
        api = WeatherAPI(city)
        self.weather, self.main, self.wind, self.clouds, self.sys = api.get_location()
        self.display_data()

    def display_data(self):
        print(self.weather)
        print(self.main)
        print(self.wind)
        print(self.clouds)
        print(self.sys)

obj = weather_app()
obj.layout()
