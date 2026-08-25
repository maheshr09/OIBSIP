import webbrowser
from src.audio.speaker import speak

def handle_web_search(query):
    search_term = query.replace("search", "").strip()
    if search_term:
        speak(f"Searching the web for {search_term}")
        url = f"https://www.google.com/search?q={search_term}"
        webbrowser.open(url)
    else:
        speak("What would you like me to search for?")

