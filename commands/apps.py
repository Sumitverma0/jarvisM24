import os
from voice.text_to_speech import speak

def open_notepad():
    speak("Opening Notepad")
    os.system("notepad.exe")

def open_vscode():
    speak("Opening Visual Studio Code")
    os.system("code")

def open_explorer():
    speak("Opening File Explorer")
    os.system("explorer")

def open_chrome():
    speak("Opening Google Chrome")
    os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
