import speech_recognition as sr
from src.responses import speak

def listen():
    """Captures audio from the microphone and returns the recognized text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # Adjust for ambient noise to improve recognition accuracy
        recognizer.adjust_for_ambient_noise(source)
        try:
            # Listen for up to 5 seconds before giving up
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            # Use Google's free speech recognition API
            text = recognizer.recognize_google(audio)
            print(f"Recognized: {text}")
            return text.lower()
        except sr.UnknownValueError:
            # Speech was heard but could not be understood
            print("Speech unclear.")
            speak("Sorry, I did not understand that. Could you please repeat?")
            return None
        except sr.RequestError:
            # The API is unreachable or returned an error
            print("API unavailable.")
            speak("Sorry, my speech service is currently down.")
            return None
        except sr.WaitTimeoutError:
            # No speech was detected within the timeout
            print("Listening timed out.")
            return None
        except Exception as e:
            # Catch-all for any other unexpected errors (prevents crashing)
            print(f"Error: {e}")
            return None
