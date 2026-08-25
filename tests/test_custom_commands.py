import unittest
import os
import json
from unittest.mock import patch, mock_open
from src.custom_commands import load_config, handle_custom_command

class TestCustomCommands(unittest.TestCase):
    
    def test_load_config_valid(self):
        valid_json = '{"commands": [{"trigger": "test", "action_type": "speak", "action_value": "hello"}]}'
        with patch("builtins.open", mock_open(read_data=valid_json)):
            with patch("os.path.exists", return_value=True):
                config = load_config()
                self.assertEqual(len(config), 1)
                self.assertEqual(config[0]["trigger"], "test")

    def test_load_config_invalid_json(self):
        invalid_json = '{malformed: json}'
        with patch("builtins.open", mock_open(read_data=invalid_json)):
            with patch("os.path.exists", return_value=True):
                config = load_config()
                self.assertEqual(config, [])
                
    def test_load_config_file_missing(self):
        with patch("os.path.exists", return_value=False):
            config = load_config()
            self.assertEqual(config, [])

    @patch('src.custom_commands.webbrowser.open')
    @patch('src.custom_commands.speak')
    def test_handle_custom_command(self, mock_speak, mock_webbrowser):
        config = [
            {"trigger": "open google", "action_type": "open_url", "action_value": "https://google.com"},
            {"trigger": "say hi", "action_type": "speak", "action_value": "hi there"}
        ]
        
        # Test exact match
        self.assertTrue(handle_custom_command("open google", config))
        mock_webbrowser.assert_called_with("https://google.com")
        
        # Test subset match (user says something extra)
        self.assertTrue(handle_custom_command("assistant please say hi", config))
        mock_speak.assert_called_with("hi there")
        
        # Test no match
        self.assertFalse(handle_custom_command("dance", config))

if __name__ == '__main__':
    unittest.main()
