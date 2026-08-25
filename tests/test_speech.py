import unittest
from unittest.mock import patch, MagicMock
from src.speech import listen
import speech_recognition as sr

class TestSpeechRecognition(unittest.TestCase):
    
    @patch('src.speech.sr.Recognizer')
    @patch('src.speech.sr.Microphone')
    @patch('src.speech.speak')
    def test_listen_success(self, mock_speak, mock_mic, mock_recognizer_class):
        mock_recognizer = MagicMock()
        mock_recognizer_class.return_value = mock_recognizer
        mock_recognizer.recognize_google.return_value = "Hello Assistant"
        
        result = listen()
        self.assertEqual(result, "hello assistant")
        mock_speak.assert_not_called()

    @patch('src.speech.sr.Recognizer')
    @patch('src.speech.sr.Microphone')
    @patch('src.speech.speak')
    def test_listen_unclear_speech(self, mock_speak, mock_mic, mock_recognizer_class):
        mock_recognizer = MagicMock()
        mock_recognizer_class.return_value = mock_recognizer
        # Simulate mumbling/unclear speech
        mock_recognizer.recognize_google.side_effect = sr.UnknownValueError()
        
        result = listen()
        self.assertIsNone(result)
        mock_speak.assert_called_with("Sorry, I did not understand that. Could you please repeat?")

    @patch('src.speech.sr.Recognizer')
    @patch('src.speech.sr.Microphone')
    @patch('src.speech.speak')
    def test_listen_api_error(self, mock_speak, mock_mic, mock_recognizer_class):
        mock_recognizer = MagicMock()
        mock_recognizer_class.return_value = mock_recognizer
        # Simulate Google API down or no internet
        mock_recognizer.recognize_google.side_effect = sr.RequestError()
        
        result = listen()
        self.assertIsNone(result)
        mock_speak.assert_called_with("Sorry, my speech service is currently down.")

    @patch('src.speech.sr.Recognizer')
    @patch('src.speech.sr.Microphone')
    @patch('src.speech.speak')
    def test_listen_timeout(self, mock_speak, mock_mic, mock_recognizer_class):
        mock_recognizer = MagicMock()
        mock_recognizer_class.return_value = mock_recognizer
        # Simulate silence
        mock_recognizer.listen.side_effect = sr.WaitTimeoutError()
        
        result = listen()
        self.assertIsNone(result)
        # Timeout currently just prints to console and returns None silently

if __name__ == '__main__':
    unittest.main()
