from voice.text_to_speech import speak
from command_router import route_command
import datetime

speak("Jarvis system online.")

time = datetime.datetime.now().strftime("%I:%M %p")
speak(f"Sir, the time is {time}")

while True:
    command = input("enter your command here: ").lower()

    status = route_command(command)

    if status == "EXIT":
        break

    if status == "NOT_HANDLED":
        speak("Sorry sir, I don't know how to do that yet.")
