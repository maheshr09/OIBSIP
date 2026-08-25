import re
from src.responses import speak

# Local, offline knowledge base. Easy to extend.
# Keys are keywords/phrases to match against the user's question.
LOCAL_KNOWLEDGE = {
    "python": "Python is a high-level, interpreted programming language known for its readability.",
    "creator of python": "Python was created by Guido van Rossum and first released in 1991.",
    "capital of india": "The capital of India is New Delhi.",
    "speed of light": "The speed of light in a vacuum is approximately 299,792 kilometers per second.",
    "tallest mountain": "Mount Everest is the tallest mountain above sea level.",
    "open source": "Open source software is code that is designed to be publicly accessible so anyone can see, modify, and distribute it."
}

def clean_query(command: str) -> str:
    """Removes question triggers to extract the core topic."""
    triggers = ["who is", "what is", "tell me about", "explain", "do you know"]
    query = command.lower()
    for trigger in triggers:
        query = query.replace(trigger, "")
    return query.strip()

def fetch_answer(query: str) -> str:
    """
    Abstraction layer for fetching an answer.
    Currently searches a local dictionary. 
    Can be replaced with an external API call (like Wikipedia) in the future.
    """
    if not query:
        return None
        
    # Simple keyword matching
    for keyword, answer in LOCAL_KNOWLEDGE.items():
        # Using word boundaries to ensure we match the exact keyword phrase
        if re.search(r'\b' + re.escape(keyword) + r'\b', query, re.IGNORECASE):
            return answer
            
    return None

def handle_knowledge(command: str):
    """Handles the knowledge intent flow."""
    query = clean_query(command)
    
    if not query:
        speak("I didn't catch what you wanted me to explain.")
        return
        
    answer = fetch_answer(query)
    
    if answer:
        speak(answer)
    else:
        speak("I don't have information on that topic in my local database yet.")
