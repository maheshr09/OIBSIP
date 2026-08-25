import datetime
import webbrowser
from src.responses import speak
from src.intent_parser import parse_intent, extract_search_query
from src.custom_commands import load_config, handle_custom_command

# Load configuration once on startup
CUSTOM_COMMANDS_CONFIG = load_config()

def handle_hello():
    speak("Hello! How can I help you today?")

def handle_time():
    now = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {now}")

def handle_date():
    today = datetime.datetime.now().strftime("%B %d, %Y")
    speak(f"Today's date is {today}")

def handle_web_search(original_command):
    search_term = extract_search_query(original_command)
    if search_term:
        speak(f"Searching the web for {search_term}")
        url = f"https://www.google.com/search?q={search_term}"
        webbrowser.open(url)
    else:
        speak("What would you like me to search for?")

def process_command(command):
    """Routes the user's spoken command."""
    if not command:
        return True
        
    # Check custom user commands first!
    if handle_custom_command(command, CUSTOM_COMMANDS_CONFIG):
        return True

    intent, original_command = parse_intent(command)
    
    if intent == "UNKNOWN" and not original_command:
        # Happens when speech recognition returns None
        return True

    if intent == "EXIT":
        speak("Goodbye!")
        return False
    elif intent == "GREETING":
        handle_hello()
    elif intent == "TIME":
        handle_time()
    elif intent == "DATE":
        handle_date()
    elif intent == "WEB_SEARCH":
        handle_web_search(original_command)
    elif intent == "REMINDER":
        from src.reminder import start_reminder
        start_reminder(original_command)
    elif intent == "WEATHER":
        from src.weather import handle_weather
        handle_weather(original_command)
    elif intent == "SEND_EMAIL":
        from src.email_service import handle_email
        handle_email()
    elif intent == "KNOWLEDGE":
        from src.knowledge import handle_knowledge
        handle_knowledge(original_command)
    else:
        speak("I am not sure how to help with that yet.")
    
    return True
