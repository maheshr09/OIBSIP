import os
from dotenv import load_dotenv

# Load environment variables first
load_dotenv()

from src.speech import listen
from src.responses import speak
from src.commands import process_command

def main():
    """Main entry point for the voice assistant."""
    speak("Voice assistant initialized and ready.")
    while True:
        command = listen()
        should_continue = process_command(command)
        if not should_continue:
            break

if __name__ == "__main__":
    main()
