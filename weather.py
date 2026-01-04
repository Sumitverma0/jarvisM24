import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather(city="Noida"):
    if not API_KEY:
        return "Weather API key is missing."

    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        data = requests.get(url, params=params, timeout=5).json()

        if data.get("cod") != 200:
            return "City not found."

        main = data["main"]
        weather = data["weather"][0]
        wind = data["wind"]

        temp = main["temp"]
        feels_like = main["feels_like"]
        humidity = main["humidity"]
        description = weather["description"]
        wind_speed = wind["speed"]

        return (
            f"The current weather in {city} is {description}. "
            f"Temperature is {temp}°C, feels like {feels_like}°C. "
            f"Humidity is {humidity} percent, "
            f"and wind speed is {wind_speed} meters per second."
        )

    except Exception as e:
        return "Weather service is currently unavailable."
