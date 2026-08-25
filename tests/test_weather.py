import unittest
from unittest.mock import patch, MagicMock
from src.weather import extract_city, handle_weather
import requests

class TestWeatherFeature(unittest.TestCase):
    
    def test_extract_city(self):
        self.assertEqual(extract_city("what is the weather in Pune"), "Pune")
        self.assertEqual(extract_city("weather for London"), "London")
        self.assertEqual(extract_city("what's it like at Tokyo"), "Tokyo")
        self.assertEqual(extract_city("weather"), "")

    @patch('src.weather.speak')
    @patch('src.weather.os.environ.get')
    def test_missing_api_key(self, mock_env_get, mock_speak):
        mock_env_get.return_value = None
        handle_weather("weather in Pune")
        mock_speak.assert_called_with("My OpenWeatherMap API key is not configured. Please add it to the environment variables.")

    @patch('src.weather.speak')
    @patch('src.weather.requests.get')
    @patch('src.weather.os.environ.get')
    def test_weather_success(self, mock_env_get, mock_requests_get, mock_speak):
        mock_env_get.return_value = "fake_key"
        
        # Mock the successful JSON response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "main": {"temp": 25.5, "humidity": 60},
            "weather": [{"description": "clear sky"}]
        }
        mock_requests_get.return_value = mock_response
        
        handle_weather("weather in Pune")
        mock_speak.assert_called_with("The weather in Pune is clear sky with a temperature of 25.5 degrees Celsius and 60 percent humidity.")

    @patch('src.weather.speak')
    @patch('src.weather.requests.get')
    @patch('src.weather.os.environ.get')
    def test_invalid_city(self, mock_env_get, mock_requests_get, mock_speak):
        mock_env_get.return_value = "fake_key"
        
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_requests_get.return_value = mock_response
        
        handle_weather("weather in FakeCity")
        mock_speak.assert_called_with("I couldn't find weather information for FakeCity.")

    @patch('src.weather.speak')
    @patch('src.weather.requests.get')
    @patch('src.weather.os.environ.get')
    def test_invalid_api_key(self, mock_env_get, mock_requests_get, mock_speak):
        mock_env_get.return_value = "bad_key"
        
        mock_response = MagicMock()
        mock_response.status_code = 401
        mock_requests_get.return_value = mock_response
        
        handle_weather("weather in Pune")
        mock_speak.assert_called_with("My OpenWeatherMap API key is invalid or unauthorized.")

    @patch('src.weather.speak')
    @patch('src.weather.requests.get')
    @patch('src.weather.os.environ.get')
    def test_network_failure(self, mock_env_get, mock_requests_get, mock_speak):
        mock_env_get.return_value = "fake_key"
        
        # Simulate a network drop
        mock_requests_get.side_effect = requests.exceptions.RequestException("Network down")
        
        handle_weather("weather in Pune")
        mock_speak.assert_called_with("I'm having trouble connecting to the weather service right now.")

if __name__ == '__main__':
    unittest.main()
