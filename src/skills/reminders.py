import threading
import time
from src.audio.speaker import speak

def reminder_thread(seconds, message):
    time.sleep(seconds)
    speak(f"Reminder: {message}")
    print("\a") # System beep

def handle_reminder():
    speak("Setting a demo reminder for 10 seconds.")
    t = threading.Thread(target=reminder_thread, args=(10, "This is your reminder!"))
    t.daemon = True
    t.start()

