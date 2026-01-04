import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)  # speed
    engine.setProperty('volume', 1)  # loudness
    engine.say(text)
    engine.runAndWait()

# test
if __name__ == "__main__":
    speak("Hello Sumit! I am JARVIS-Vision. Let's build this project together.")
