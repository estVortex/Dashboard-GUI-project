import tkinter as tk
import requests
from utils import add_hover
from utils import api_key

class WeatherFrame(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg="#212121")
        self.app = app
        
        # Weather state when launching
        self.weather_data = None
        self.is_celsius = True
        self.is_kmph = True
        self.data_type = "temperature"
        
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the weather frame UI."""
        for i in range(7):
            self.columnconfigure(i, weight=1)
            self.rowconfigure(i, weight=1)
        
        # Weather label
        weatherlabel = tk.Label(
            self,
            text="Weather",
            font=("Arial", 20),
            bg="#171717",
            fg="#ffffff"
        )
        weatherlabel.grid(row=0, column=1, sticky="ewn", columnspan=5, padx=10, pady=10)
        
        # Menu button
        menu_button = tk.Button(
            self,
            text="Menu",
            font=("Arial", 20),
            bg="#303030",
            fg="#ffffff",
            activebackground="#404040",
            activeforeground="#ffffff",
            command=lambda: self.app.show_frame(self.app.menu_frame)
        )
        menu_button.grid(row=0, column=0, sticky="nw")
        add_hover(menu_button, "#3a3a3a", "#303030")
        
        # Location entry
        self.location_entry = tk.Entry(
            self,
            text="Weather",
            font=("Arial", 20),
            bg="#171717",
            fg="#ffffff",
            justify="center"
        )
        self.location_entry.grid(row=1, column=1, columnspan=5, sticky="new", padx=10, pady=10)
        self.location_entry.bind("<Return>", self.get_weather)
        
        # Data type button
        databtn = tk.Button(
            self,
            text="Datatype",
            font=("Arial", 20),
            bg="#303030",
            fg="#ffffff",
            activebackground="#404040",
            activeforeground="#ffffff",
            command=self.switch_data
        )
        databtn.grid(row=2, column=1, sticky="news", padx=10, pady=10, columnspan=2)
        
        # Units button
        unitsbtn = tk.Button(
            self,
            text="Units",
            font=("Arial", 20),
            bg="#303030",
            fg="#ffffff",
            activebackground="#404040",
            activeforeground="#ffffff",
            command=self.switch_units
        )
        unitsbtn.grid(row=2, column=3, sticky="news", padx=10, pady=10)
        
        # Get data button
        timebtn = tk.Button(
            self,
            text="Get Data",
            font=("Arial", 20),
            bg="#303030",
            fg="#ffffff",
            activebackground="#404040",
            activeforeground="#ffffff",
            command=self.get_weather
        )
        timebtn.grid(row=2, column=4, sticky="news", padx=10, pady=10, columnspan=2)
        
        # Weather stats display
        self.weatherstats = tk.Label(
            self,
            text="",
            font=("Arial", 20),
            bg="#303030",
            fg="#ffffff"
        )
        self.weatherstats.grid(row=3, column=1, columnspan=5, sticky="nsew", padx=10, pady=10)
    
    def get_weather(self, event=None):
        """Fetch weather data from API."""
        location = str(self.location_entry.get()).capitalize()
        url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=no"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                self.weather_data = response.json()
                self.show_weather()
            else:
                self.weatherstats.config(text="Error")
        except Exception as e:
            self.weatherstats.config(text=f"Error: {str(e)}")
    
    def show_weather(self):
        """Display weather data based on current data type."""
        if self.weather_data is None:
            return
        
        if self.data_type == "temperature":
            if self.is_celsius:
                self.weatherstats.config(text=f"{self.weather_data['current']['temp_c']}°C")
            else:
                self.weatherstats.config(text=f"{self.weather_data['current']['temp_f']}°F")
        elif self.data_type == "wind_speed":
            if self.is_kmph:
                self.weatherstats.config(text=f"{self.weather_data['current']['wind_kph']}km/h")
            else:
                self.weatherstats.config(text=f"{self.weather_data['current']['wind_mph']}mi/h")
        elif self.data_type == "humidity":
            self.weatherstats.config(text=f"{self.weather_data['current']['humidity']}% humidity")
        elif self.data_type == "uv":
            self.weatherstats.config(text=f"{self.weather_data['current']['uv']} uv index")
    
    def switch_units(self):
        """Toggle between different units."""
        if self.weather_data is None:
            return
        
        if self.data_type == "temperature":
            self.is_celsius = not self.is_celsius
        elif self.data_type == "wind_speed":
            self.is_kmph = not self.is_kmph
        
        self.show_weather()
    
    def switch_data(self):
        """Switch between different data types."""
        if self.data_type == "temperature":
            self.data_type = "wind_speed"
        elif self.data_type == "wind_speed":
            self.data_type = "humidity"
        elif self.data_type == "humidity":
            self.data_type = "uv"
        elif self.data_type == "uv":
            self.data_type = "temperature"
        
        self.show_weather()