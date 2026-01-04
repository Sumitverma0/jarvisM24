from voice.text_to_speech import speak
from vision import start_face_detection, take_screenshot

def vision_mode():
    speak("Activating vision mode")
    start_face_detection()

def take_photo():
    speak("Taking picture")
    take_screenshot()
