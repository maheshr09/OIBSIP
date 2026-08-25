import requests
from src.utils.config_loader import load_config
from src.audio.speaker import speak

def handle_weather(command):
    config = load_config()
    api_key = config.get("openweathermap_api_key")
    
    if not api_key:
        speak("Weather API key is not configured.")
        return
    
    city = "London" # Extract from command ideally
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        if data.get("cod") != 200:
            speak("Could not fetch weather data.")
            return
        
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        speak(f"The weather in {city} is {desc} with a temperature of {temp} degrees Celsius.")
    except Exception as e:
        speak("Error fetching weather information.")

