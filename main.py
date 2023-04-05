import tkinter as tk
import requests
import time

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
        
        self.clock = tk.Label(self.window, font=("Calibri", 40), bg="#DADAA5", fg="white")
        self.clock.place(x=500, y=50, height=50, width=350)
        
        self.l1_WeatherUp = tk.Label(self.window, font=("Calibri", 40), bg='#DADAA5', fg='white')
        self.l1_WeatherUp.place(x=520, y=450, height=100, width=540)
    
    def layout(self):
        name_label = tk.Label(self.window, text="Check Weather", font=("calibri", 30, "bold"), bg='#DADAA5', fg='white').place(x=100, y=50, height=50, width=350)
        
        # city_name = StringVar()

        city_entry = tk.Entry(self.window, font=("calibri", 20, "bold")).place(x=100, y=150, height=30, width=200)
        fetch_data = tk.Button(self.window, text="Fetch Data", command=self.get_data).place(x=320, y=150, height=30, width=150)

        # Left Layout
        tk.Label(self.window, text="Temperature Details", font=("calibri", 10, "bold"), anchor="center").place(x=200, y=260, height=30, width=200)

        tk.Label(self.window, text="Current Temperature", font=("calibri", 10, "bold"), anchor="w").place(x=100, y=300, height=30, width=180)
        self.currtemp = tk.Label(self.window, text="", font=("calibri", 10)).place(x=320, y=300, height=30, width=150)

        tk.Label(self.window, text="Min Temperature", font=("calibri", 10, "bold"), anchor="w").place(x=100, y=340, height=30, width=180)
        self.mintemp = tk.Label(self.window, text="", font=("calibri", 10)).place(x=320, y=340, height=30, width=150)

        tk.Label(self.window, text="Max Temperature", font=("calibri", 10, "bold"), anchor="w").place(x=100, y=380, height=30, width=180)
        self.maxtemp = tk.Label(self.window, text="", font=("calibri", 10)).place(x=320, y=380, height=30, width=150)


        # Right Layout

        tk.Label(self.window, text="Other Details", font=("calibri", 10, "bold"), anchor="center").place(x=650, y=150, height=30, width=200)

        tk.Label(self.window, text="Feels Like", font=("calibri", 10, "bold"), anchor="w").place(x=600, y=190, height=30, width=150)
        self.feelslike = tk.Label(self.window, text="", font=("calibri", 10)).place(x=800, y=190, height=30, width=150)

        tk.Label(self.window, text="Sunrise Time", font=("calibri", 10, "bold"), anchor="w").place(x=600, y=230, height=30, width=150)
        self.sunrise = tk.Label(self.window, text="", font=("calibri", 10)).place(x=800, y=230, height=30, width=150)

        tk.Label(self.window, text="Sunset Time", font=("calibri", 10, "bold"), anchor="w").place(x=600, y=270, height=30, width=150)
        self.sunset = tk.Label(self.window, text="", font=("calibri", 10)).place(x=800, y=270, height=30, width=150)

        tk.Label(self.window, text="Windspeed", font=("calibri", 10, "bold"), anchor="w").place(x=600, y=310, height=30, width=150)
        self.windspeed = tk.Label(self.window, text="", font=("calibri", 10)).place(x=800, y=310, height=30, width=150)
        
        tk.Label(self.window, text="Pressure", font=("calibri", 10, "bold"), anchor="w").place(x=600, y=350, height=30, width=150)
        self.pressure = tk.Label(self.window, text="", font=("calibri", 10)).place(x=800, y=350, height=30, width=150)

        tk.Label(self.window, text="Weather Status", font=("calibri", 10, "bold"), anchor="w").place(x=600, y=390, height=30, width=150)
        self.status = tk.Label(self.window, text="", font=("calibri", 10)).place(x=800, y=390, height=30, width=150)

    def get_data(self):
        city=self.city_entry.get()
        data = requests.get(
            "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=20a01944eda34a13f4a4dcecfff77197").json()
        self.w_label1.config(text=data["weather"][0]["description"])
        self.wd_label1.config(text=data["weather"][0]["description"])
        self.t_label1.config(text=str(int(data["main"]["temp"]-273))+"*C"+" "+"/"+" "+str(int(data["main"]["temp"]-459))+"*F")
        self.wp1_label.config(text=data["main"]["pressure"])
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

if __name__ == "__main__":
    root = tk.Tk()
    obj = WeatherApp(root)
    obj.layout()
    obj.get_time()
    root.mainloop()

