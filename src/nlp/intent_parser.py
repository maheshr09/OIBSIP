import re

INTENTS = {
    "greeting": r"\b(hello|hi|hey|greetings)\b",
    "time": r"\b(time|clock)\b",
    "date": r"\b(date|today|day)\b",
    "search": r"\b(search|find|google)\b",
    "email": r"\b(email|mail|send message)\b",
    "reminder": r"\b(remind|reminder|alarm)\b",
    "weather": r"\b(weather|forecast|temperature)\b",
    "knowledge": r"\b(who is|what is|tell me about)\b",
    "exit": r"\b(stop|exit|quit|goodbye|bye)\b"
}

def get_intent(command):
    if not command:
        return None, None
    for intent, pattern in INTENTS.items():
        match = re.search(pattern, command, re.IGNORECASE)
        if match:
            return intent, command
    return "custom", command  # Fallback to custom commands or unknown

