import webbrowser
from voice.text_to_speech import speak
from voice.speech_to_text import listen

def open_youtube():
    speak("Opening YouTube")
    webbrowser.open("https://www.youtube.com")

def google_search():
    speak("What should I search?")
    query = listen().lower()
    if query:
        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak(f"Here are the results for {query}")
