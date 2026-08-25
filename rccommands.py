warning: in the working copy of 'main.py', LF will be replaced by CRLF the next time Git touches it
[1mdiff --git a/main.py b/main.py[m
[1mindex fb0941a..459083f 100644[m
[1m--- a/main.py[m
[1m+++ b/main.py[m
[36m@@ -1,45 +1,21 @@[m
[31m-from src.audio.recognizer import listen[m
[31m-from src.audio.speaker import speak[m
[31m-from src.skills.core import handle_hello, handle_time, handle_date[m
[31m-from src.skills.search import handle_web_search[m
[32m+[m[32mimport os[m
[32m+[m[32mfrom dotenv import load_dotenv[m
 [m
[31m-def process_command(command):[m
[31m-    """Routes the user's spoken command to the appropriate beginner skill."""[m
[31m-    if not command:[m
[31m-        # If command is None, an error occurred in speech recognition (already handled gracefully)[m
[31m-        return True[m
[32m+[m[32m# Load environment variables first[m
[32m+[m[32mload_dotenv()[m
 [m
[31m-    # Use simple string matching for beginner requirements[m
[31m-    if "stop" in command or "exit" in command:[m
[31m-        speak("Goodbye!")[m
[31m-        return False # This will break the listening loop[m
[31m-    elif "hello" in command:[m
[31m-        handle_hello()[m
[31m-    elif "time" in command:[m
[31m-        handle_time()[m
[31m-    elif "date" in command:[m
[31m-        handle_date()[m
[31m-    elif "search" in command:[m
[31m-        handle_web_search(command)[m
[31m-    else:[m
[31m-        # Graceful fallback for unknown commands[m
[31m-        speak("I am not sure how to help with that yet.")[m
[31m-    return True[m
[32m+[m[32mfrom src.speech import listen[m
[32m+[m[32mfrom src.responses import speak[m
[32m+[m[32mfrom src.commands import process_command[m
 [m
 def main():[m
[31m-    """Main entry point for the beginner voice assistant."""[m
[31m-    speak("Beginner voice assistant initialized and ready.")[m
[32m+[m[32m    """Main entry point for the voice assistant."""[m
[32m+[m[32m    speak("Voice assistant initialized and ready.")[m
     while True:[m
[31m-        # 1. Listen for audio input[m
         command = listen()[m
[31m-        [m
[31m-        # 2. Process the recognized command[m
         should_continue = process_command(command)[m
[31m-        [m
[31m-        # 3. Exit the program if told to stop[m
         if not should_continue:[m
             break[m
 [m
 if __name__ == "__main__":[m
     main()[m
[31m-[m
