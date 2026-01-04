from voice.text_to_speech import speak
from voice.speech_to_text import listen
from gemini_ai import ask_gemini

def ai_mode():
    while True:
        speak("What would you like to ask?")
        # query = listen()
        query = input("enter what you want to ask")
        if "nothing" in query:
            speak("Exiting AI mode.")
            break
        if query:
            speak(ask_gemini(query))
