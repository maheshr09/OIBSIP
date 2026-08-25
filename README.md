# Python Voice Assistant

## 1. Project Title
**Python Voice Assistant**

## 2. Project Overview
The Python Voice Assistant is a desktop-based application built to understand and respond to spoken commands. It leverages natural language interactions to perform fundamental tasks such as fetching the time and date, managing basic greetings, and executing web searches.

## 3. Objective
This project was developed as part of an internship to build a scalable and modular voice-operated assistant using Python. The primary goal is to create a beginner-friendly foundation for audio input and text-to-speech output that can easily be extended with advanced capabilities in the future.

## 4. Features Currently Implemented
The following foundational ("Beginner") features are fully implemented and functional:
- **Microphone Input:** Captures and translates user speech into text.
- **Text-to-Speech (TTS):** Responds to the user audibly with a synthesized voice.
- **Continuous Listening:** The main program continuously listens for commands until instructed to stop.
- **Basic Greetings:** Responds appropriately when the user says "hello".
- **Time and Date:** Audibly announces the current time and today's date upon request.
- **Web Searching:** Parses commands like "search Python tutorials" and automatically opens the default web browser to a Google search for the requested topic.
- **Polite Reprompting:** If the user's speech is unclear or unrecognized, the assistant gracefully asks the user to repeat the command.

## 5. Technologies Used
- **Python 3.13** - Core programming language
- **SpeechRecognition** - Library used to capture audio and interface with the Google Web Speech API
- **PyAudio** - Required by SpeechRecognition for microphone stream management
- **pyttsx3** - Offline text-to-speech conversion library
- **Webbrowser** - Built-in Python module to launch external web searches

## 6. Project Structure
The repository is designed with a modular architecture to ensure clean separation of concerns:

`	ext
INtrenship/
+-- venv/                      # Virtual environment (ignored by Git)
+-- .gitignore                 # Specifies intentionally untracked files
+-- requirements.txt           # Project dependencies
+-- README.md                  # This documentation file
+-- main.py                    # Entry point for the application
+-- config.json                # API keys and custom settings
+-- src/                       # Source code directory
    +-- audio/                 # Audio capture and synthesis modules
    ¦   +-- recognizer.py      # Speech-to-text logic
    ¦   +-- speaker.py         # Text-to-speech logic
    +-- skills/                # Capabilities of the assistant
    ¦   +-- core.py            # Hello, time, date handlers
    ¦   +-- search.py          # Web search functionality
    +-- nlp/                   # (Future) Intent recognition module
    +-- utils/                 # Utilities like configuration loaders
`
*(Note: Some directories contain boilerplate files in preparation for future advanced features.)*

## 7. Installation Instructions

1. **Clone the repository:**
   *(See GitHub usage instructions below)*

2. **Set up a Virtual Environment:**
   It is highly recommended to isolate the project dependencies.
   `powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1   # On Windows
   `

3. **Install Dependencies:**
   Ensure pip is up to date, then install the required packages.
   `powershell
   pip install -r requirements.txt
   `

## 8. How to Run the Project
Ensure your virtual environment is active and your microphone is plugged in and recognized by your system.

Navigate to the root directory of the project and execute:
`powershell
python main.py
`
You will hear the assistant announce that it is initialized and ready. Wait for the terminal to display Listening... before speaking.

## 9. Example Voice Commands
Try speaking the following phrases into your microphone:
- *"Hello"* (The assistant will greet you)
- *"What is the time?"* (The assistant will state the current time)
- *"Tell me today's date"* (The assistant will state the date)
- *"Search for Python tutorials"* (The assistant will open a Google search for 'Python tutorials')
- *"Exit"* or *"Stop"* (The assistant will say goodbye and terminate)

## 10. Error Handling
The application is built to be robust and will not crash under normal failure conditions:
- **Unrecognized Speech:** Catches UnknownValueError. The assistant politely asks you to repeat yourself.
- **Network Issues:** Catches RequestError. If the Google Speech API cannot be reached, the assistant informs you that its service is down.
- **Timeout:** Catches WaitTimeoutError. If no speech is detected after a few seconds, the assistant simply restarts the listening loop.

## 11. Current Limitations
- The intent matching is currently based on simple string keyword matching (e.g., checking if the word "time" is in the command).
- An active internet connection is required for the speech-to-text functionality (Google Web Speech API).
- It does not yet integrate with external data sources for advanced queries (like weather or Wikipedia).

## 12. Future Enhancements
The following advanced features are planned for subsequent phases of the internship:
- **Natural Language Intent Recognition:** Transitioning from simple keyword matching to regex/NLP-based intent parsing.
- **Email Integration:** Sending emails using smtplib.
- **Reminders:** Background timed reminders with audible alerts.
- **Live Weather Updates:** Integration with the OpenWeatherMap API.
- **General Knowledge QA:** Answering facts using Wikipedia or similar APIs.
- **Custom Commands:** Allowing the user to map specific phrases to executable scripts via config.json.

## 13. Privacy Considerations
This assistant processes your audio and executes actions on your local machine. However, because it relies on the Google Web Speech API for transcription, your audio snippets are sent to Google's servers for processing. Additionally, the web search feature transmits your search terms to external search engines. Future offline speech recognition models (like Vosk) may be evaluated if strict offline privacy is required.

## 14. GitHub Usage Instructions
If you plan to contribute or manage versions of this project, you can use Git:
1. Initialize git (if not already done): git init
2. Add files: git add .
3. Commit changes: git commit -m "Initial commit of Phase 1"
4. Link to remote repository: git remote add origin <your-repo-url>
5. Push to GitHub: git push -u origin main

*Ensure you do not commit your env/ folder or config.json containing sensitive keys (these are already included in .gitignore).*

## 15. Author
Developed by **Mahesh** as part of a Python Voice Assistant Internship Project.
