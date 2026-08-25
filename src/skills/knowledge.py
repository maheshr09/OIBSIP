import wikipedia
from src.audio.speaker import speak

def handle_knowledge(command):
    query = command.replace("who is", "").replace("what is", "").replace("tell me about", "").strip()
    if not query:
        speak("Please specify what you want to know.")
        return
    
    speak(f"Looking up {query} on Wikipedia.")
    try:
        result = wikipedia.summary(query, sentences=2)
        speak(result)
    except wikipedia.exceptions.DisambiguationError as e:
        speak("There are multiple results, please be more specific.")
    except wikipedia.exceptions.PageError:
        speak("I could not find any information on that topic.")
    except Exception as e:
        speak("An error occurred while fetching knowledge.")

