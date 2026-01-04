from commands.system import wake, tell_time, battery, exit_jarvis
from commands.apps import open_notepad, open_vscode, open_explorer, open_chrome
from commands.web import open_youtube, google_search
from commands.vision_cmd import vision_mode, take_photo
from commands.ai import ai_mode
from commands.weater_cmd import weather_info


COMMANDS = {
    "jarvis": wake,
    "time": tell_time,
    "battery": battery,
    "open youtube": open_youtube,
    "search": google_search, 
    "open notepad": open_notepad,
    "open vs code": open_vscode,
    "open code": open_vscode,
    "open explorer": open_explorer,
    "open file explorer": open_explorer,
    "open chrome": open_chrome,
    "vision mode": vision_mode,
    "start face detection": vision_mode,
    "photo": take_photo,
    "take picture": take_photo,
    "weather": weather_info,
    "temperature": weather_info,
    "ask": ai_mode, 
    "answer": ai_mode,
    "exit": exit_jarvis,
    "stop": exit_jarvis,
    "bye": exit_jarvis,
}

def route_command(command: str):
    for key, handler in COMMANDS.items():
        if key in command:
            result = handler()
            if result == "EXIT":
                return "EXIT"
            return "HANDLED"
    return "NOT_HANDLED"
