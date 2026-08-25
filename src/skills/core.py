import datetime
from src.audio.speaker import speak

def handle_hello():
    speak("Hello! How can I help you today?")

def handle_time():
    now = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {now}")

def handle_date():
    today = datetime.datetime.now().strftime("%B %d, %Y")
    speak(f"Today's date is {today}")

