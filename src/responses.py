import pyttsx3

def speak(text):
    """Converts text to speech and plays it aloud."""
    print(f"Assistant: {text}")
    try:
        # Initialize the text-to-speech engine
        engine = pyttsx3.init()
        # Queue the text to be spoken
        engine.say(text)
        # Block execution and play the audio
        engine.runAndWait()
    except Exception as e:
        # Handle errors gracefully without crashing the program
        print(f"Error in TTS: {e}")
