import requests
import matplotlib.pyplot as plt
import matplotlib
from datetime import datetime

matplotlib.use('TkAgg')  
API_KEY = '869e2a41779e43c26fb46c42138c0366'

CITY = 'Goa'
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()
if response.status_code != 200:
    print(f"Error: {response.status_code}, Message: {data.get('message', 'No message')}")
    exit()
if 'list' not in data:
    print("Error: Weather data not found. Check city name or API key.")
    exit()
temperatures = []
timestamps = []
for entry in data['list']:
    temperatures.append(entry['main']['temp'])
    timestamps.append(datetime.strptime(entry['dt_txt'], '%Y-%m-%d %H:%M:%S'))
plt.figure(figsize=(10, 5))
plt.plot(timestamps, temperatures, marker='o', linestyle='-', color='teal')
plt.title(f"5-Day Temperature Forecast for {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("weather_forecast.png")
plt.show()
print("Plot saved as weather_forecast.png")