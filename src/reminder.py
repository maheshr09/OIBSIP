import re
import threading
from src.responses import speak

def parse_duration(command: str) -> int:
    """
    Extracts time duration from a string and returns the total in seconds.
    Supports seconds, minutes, and hours.
    Returns 0 if no valid duration is found.
    """
    total_seconds = 0
    
    # Define regex patterns for different units
    # Matches a number (integer or decimal) followed optionally by spaces and the unit
    sec_match = re.search(r'(\d+(?:\.\d+)?)\s*(?:sec|secs|second|seconds)\b', command, re.IGNORECASE)
    min_match = re.search(r'(\d+(?:\.\d+)?)\s*(?:min|mins|minute|minutes)\b', command, re.IGNORECASE)
    hr_match = re.search(r'(\d+(?:\.\d+)?)\s*(?:hr|hrs|hour|hours)\b', command, re.IGNORECASE)
    
    if hr_match:
        total_seconds += float(hr_match.group(1)) * 3600
    if min_match:
        total_seconds += float(min_match.group(1)) * 60
    if sec_match:
        total_seconds += float(sec_match.group(1))
        
    return int(total_seconds)

def _play_alert():
    """Callback function executed when the timer finishes."""
    speak("Ding! This is your reminder.")
    # You could also add a system beep here: print('\a')

def start_reminder(command: str) -> bool:
    """
    Parses the command for a duration and starts a background timer.
    Returns True if successfully started, False if the duration was invalid.
    """
    duration_secs = parse_duration(command)
    
    if duration_secs <= 0:
        speak("I'm sorry, I couldn't figure out the duration for that reminder.")
        return False
        
    # Start a background timer
    timer = threading.Timer(duration_secs, _play_alert)
    timer.daemon = True # Ensure it doesn't block the program from exiting
    timer.start()
    
    speak(f"Reminder set for {duration_secs} seconds from now.")
    return True
