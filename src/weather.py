import os
import re
import requests
from src.responses import speak

def extract_city(command: str) -> str:
    """
    Extracts the city name from a weather-related command.
    Matches phrases like 'weather in Pune' or 'weather for Pune'.
    """
    match = re.search(r'\b(?:in|for|at)\s+([a-zA-Z\s]+)', command, re.IGNORECASE)
    if match:
        # Return the city name, stripping any trailing spaces or punctuation
        return match.group(1).strip()
    return ""

def handle_weather(command: str):
    """
    Fetches the current weather for a specified city and speaks the result.
    """
    api_key = os.environ.get("OPENWEATHERMAP_API_KEY")
    if not api_key:
        speak("My OpenWeatherMap API key is not configured. Please add it to the environment variables.")
        return

    city = extract_city(command)
    if not city:
        speak("Which city would you like the weather for?")
        return

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Use Celsius
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        
        # Check for specific HTTP errors
        if response.status_code == 404:
            speak(f"I couldn't find weather information for {city}.")
            return
        elif response.status_code == 401:
            speak("My OpenWeatherMap API key is invalid or unauthorized.")
            return
        
        # Raise an exception for other bad status codes
        response.raise_for_status()
        
        data = response.json()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        desc = data["weather"][0]["description"]
        
        speak(f"The weather in {city} is {desc} with a temperature of {temp} degrees Celsius and {humidity} percent humidity.")
        
    except requests.exceptions.RequestException as e:
        # Sanitize error logging to prevent API key exposure
        print("Network or API error occurred while fetching weather.")
        speak("I'm having trouble connecting to the weather service right now.")
    except Exception as e:
        print("An unexpected error occurred while fetching weather.")
        speak("Sorry, I encountered an error while getting the weather.")
