from src.audio.recognizer import listen
from src.audio.speaker import speak
from src.skills.core import handle_hello, handle_time, handle_date
from src.skills.search import handle_web_search

def process_command(command):
    """Routes the user's spoken command to the appropriate beginner skill."""
    if not command:
        # If command is None, an error occurred in speech recognition (already handled gracefully)
        return True

    # Use simple string matching for beginner requirements
    if "stop" in command or "exit" in command:
        speak("Goodbye!")
        return False # This will break the listening loop
    elif "hello" in command:
        handle_hello()
    elif "time" in command:
        handle_time()
    elif "date" in command:
        handle_date()
    elif "search" in command:
        handle_web_search(command)
    else:
        # Graceful fallback for unknown commands
        speak("I am not sure how to help with that yet.")
    return True

def main():
    """Main entry point for the beginner voice assistant."""
    speak("Beginner voice assistant initialized and ready.")
    while True:
        # 1. Listen for audio input
        command = listen()
        
        # 2. Process the recognized command
        should_continue = process_command(command)
        
        # 3. Exit the program if told to stop
        if not should_continue:
            break

if __name__ == "__main__":
    main()

