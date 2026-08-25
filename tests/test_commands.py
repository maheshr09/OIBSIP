import unittest
from unittest.mock import patch
from src.commands import process_command

class TestCommandRouting(unittest.TestCase):

    @patch('src.commands.handle_hello')
    def test_route_greeting(self, mock_hello):
        process_command("hello")
        mock_hello.assert_called_once()

    @patch('src.commands.handle_time')
    def test_route_time(self, mock_time):
        process_command("what time is it")
        mock_time.assert_called_once()

    @patch('src.commands.handle_date')
    def test_route_date(self, mock_date):
        process_command("what is today's date")
        mock_date.assert_called_once()

    @patch('src.commands.handle_web_search')
    def test_route_search(self, mock_search):
        process_command("search for python")
        mock_search.assert_called_once_with("search for python")

    @patch('src.commands.speak')
    def test_route_exit(self, mock_speak):
        result = process_command("stop")
        self.assertFalse(result)
        mock_speak.assert_called_with("Goodbye!")

    @patch('src.reminder.start_reminder')
    def test_route_reminder(self, mock_reminder):
        process_command("remind me in 5 minutes")
        mock_reminder.assert_called_once_with("remind me in 5 minutes")

    @patch('src.weather.handle_weather')
    def test_route_weather(self, mock_weather):
        process_command("what is the weather in Pune")
        mock_weather.assert_called_once_with("what is the weather in pune")
        
    @patch('src.email_service.handle_email')
    def test_route_email(self, mock_email):
        process_command("send an email")
        mock_email.assert_called_once()

    @patch('src.knowledge.handle_knowledge')
    def test_route_knowledge(self, mock_knowledge):
        process_command("who is the creator of python")
        mock_knowledge.assert_called_once_with("who is the creator of python")

if __name__ == '__main__':
    unittest.main()
