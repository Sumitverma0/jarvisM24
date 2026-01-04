import psutil
# from voice.text_to_speech import speak

def get_battery_status():
    battery = psutil.sensors_battery()
    percent = battery.percent
    is_plugged = battery.power_plugged

    status = f"sir the total battery power is {percent} percent."
    if is_plugged:
        status += " Your system is charging."
    else:
        status += " Your system is not charging."
        if percent < 20:
            status += " Please plug in your charger soon."
    return status

# speak(get_battery_status())