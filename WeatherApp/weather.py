import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    print("⚠️ API key not found. Please check your .env file.")
    exit()

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url)
    data = response.json()
except:
    print("⚠️ Unable to connect to weather service.")
    exit()

if data["cod"] == 200:

    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]

    if "clear" in description:
        emoji = "☀️"
    elif "cloud" in description:
        emoji = "☁️"
    elif "rain" in description:
        emoji = "🌧️"
    elif "snow" in description:
        emoji = "❄️"
    else:
        emoji = "🌍"

    print("\n==============================")
    print("        WEATHER REPORT")
    print("==============================")
    print("City:", city)
    print(f"Condition: {description} {emoji}")
    print("Temperature:", temp, "°C")
    print("Humidity:", humidity, "%")
    print("Wind Speed:", wind_speed, "m/s")
    print("==============================")

else:
    print("❌ City not found. Please try again.")