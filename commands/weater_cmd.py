from voice.text_to_speech import speak
from weather import get_weather

def weather_info():
    weather = get_weather("Noida")
    speak(weather)
