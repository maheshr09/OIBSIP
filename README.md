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

## 7. Installation Instructions`n`n### OpenWeatherMap API Setup`nTo use the live weather feature, you need a free OpenWeatherMap API key:`n1. Sign up at [OpenWeatherMap](https://openweathermap.org/).`n2. Go to your API keys and copy your key.`n3. Copy the `.env.example` file to a new file named `.env`.`n4. Paste your key into the `OPENWEATHERMAP_API_KEY` variable inside the `.env` file.`n`n*Never share your `.env` file or commit it to GitHub. It is safely ignored by `.gitignore`.*`n

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

### SMTP Email Setup`nTo use the email feature securely, you need an App Password (especially for Gmail):`n1. Go to your Google Account > Security.`n2. Enable 2-Step Verification if not already on.`n3. Search for "App Passwords" and generate a new one for "Mail".`n4. Copy the generated 16-character password.`n5. Open your `.env` file and set:`n   `EMAIL_ADDRESS=your_email@gmail.com``n   `EMAIL_PASSWORD=your_16_char_password``n`n*Never share your `.env` file or commit it to GitHub. If using a provider other than Gmail, you may need to modify the SMTP server in `src/email_service.py`.*`n`n### Custom Commands Setup`nUsers can add their own personalized commands without writing any Python code!`n1. Open `config/commands.json`.`n2. Add a new object to the `commands` array.`n3. Set a `trigger` (what you say), an `action_type` (e.g. `open_url`, `speak`), and the `action_value` (e.g. the URL).`n`nExample:`n```json`n{`n  "trigger": "open github",`n  "action_type": "open_url",`n  "action_value": "https://github.com"`n}`n````n*For security, the assistant will only run explicitly allowed actions and will never execute arbitrary code from this file.*`n`n## 8. How to Run the Project
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

## 16. Privacy Considerations
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




## 16. Privacy Considerations

This voice assistant is designed with privacy in mind. Please be aware of the following data flows when using the application:

* **Microphone Data & External Speech Recognition**: The application actively listens to your microphone when running. **This audio data is NOT processed locally.** The raw audio snippets are transmitted over the internet to **Google's public Speech Recognition API** (ecognize_google) to convert your speech into text.
* **Weather Data**: If you ask for the weather, the specific city name you requested is transmitted to the **OpenWeatherMap API**.
* **Email Transmission**: If you use the email feature, the recipient address, subject line, and email body are transmitted securely (via SSL) to your configured SMTP provider (e.g., Gmail). 
* **Data Storage**: The application operates entirely in memory. It **does not** intentionally record, log, or save your voice audio, spoken commands, search queries, or conversation history to your hard drive. Once the application is closed, the session data is wiped.
* **API Credentials**: Your API keys, email addresses, and passwords are only stored locally on your machine within the .env file. 
* **Security Recommendations**: 
    * **Never** commit your .env file to version control (like GitHub). It is explicitly listed in the .gitignore file to prevent this.
    * Use an "App Password" (if your email provider supports it) rather than your primary account password for the email feature.
    * Only run the voice assistant in trusted environments.


