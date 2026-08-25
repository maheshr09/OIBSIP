import re

# Dictionary mapping Intent names to a list of regex patterns.
# We use \b to match word boundaries so 'weather' doesn't match 'weathering'.
INTENT_PATTERNS = {
    "GREETING": [
        r"\b(hello|hi|hey|greetings|good morning|good afternoon|good evening)\b",
        r"\b(hi there|hey assistant)\b"
    ],
    "TIME": [
        r"\b(what time is it|current time|tell me the time)\b",
        r"\btime\b"
    ],
    "DATE": [
        r"\b(what is the date|today's date|current date|what day is it)\b",
        r"\bdate\b"
    ],
    "WEB_SEARCH": [
        r"\b(search|search for|look up|find|google)\b"
    ],
    "WEATHER": [
        r"\b(weather|temperature|forecast|how is it outside)\b"
    ],
    "REMINDER": [
        r"\b(remind|reminder|set an alarm|set a timer)\b"
    ],
    "SEND_EMAIL": [
        r"\b(email|send an email|send a message|mail)\b"
    ],
    "KNOWLEDGE": [
        r"\b(who is|what is|tell me about|explain)\b"
    ],
    "EXIT": [
        r"\b(exit|stop|quit|goodbye|bye|shut down)\b"
    ]
}

def parse_intent(command: str):
    """
    Parses a spoken command and returns the recognized intent and the cleaned text.
    Returns: (INTENT_STRING, original_command)
    """
    if not command:
        return "UNKNOWN", ""
        
    command_lower = command.lower()
    
    # Iterate through our intent dictionary
    for intent, patterns in INTENT_PATTERNS.items():
        for pattern in patterns:
            # re.IGNORECASE is used to be safe, though we already lowercased it
            if re.search(pattern, command_lower, re.IGNORECASE):
                return intent, command_lower
                
    return "UNKNOWN", command_lower

def extract_search_query(command: str) -> str:
    """Helper to remove search trigger words to get the actual query."""
    # List of phrases to remove
    triggers = ["search for", "search", "look up", "find", "google"]
    query = command.lower()
    for trigger in triggers:
        query = query.replace(trigger, "")
    return query.strip()
