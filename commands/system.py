import datetime
from voice.text_to_speech import speak
from battery_status import get_battery_status

def wake():
    speak("How can I help you, Sir.")

def tell_time():
    time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"Sir, the time is {time}")

def battery():
    speak(get_battery_status())

def exit_jarvis():
    speak("Goodbye Sir.")
    return "EXIT"
