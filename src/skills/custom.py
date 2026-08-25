import os
import subprocess
from src.utils.config_loader import load_config
from src.audio.speaker import speak

def handle_custom_command(command):
    config = load_config()
    custom_commands = config.get("custom_commands", {})
    
    for trigger, action in custom_commands.items():
        if trigger in command:
            speak(f"Executing custom command: {trigger}")
            try:
                subprocess.Popen(action, shell=True)
                return True
            except Exception as e:
                speak("Failed to execute custom command.")
                return True
    
    return False

