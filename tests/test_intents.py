import unittest
from src.intent_parser import parse_intent, extract_search_query

class TestIntentParser(unittest.TestCase):
    
    def test_greeting(self):
        self.assertEqual(parse_intent("Hello")[0], "GREETING")
        self.assertEqual(parse_intent("Hi there")[0], "GREETING")
        self.assertEqual(parse_intent("Hey assistant")[0], "GREETING")
        
    def test_time(self):
        self.assertEqual(parse_intent("What time is it?")[0], "TIME")
        self.assertEqual(parse_intent("Can you tell me the current time?")[0], "TIME")
        self.assertEqual(parse_intent("Do you know what time it is?")[0], "TIME")
        
    def test_date(self):
        self.assertEqual(parse_intent("What is the date today?")[0], "DATE")
        self.assertEqual(parse_intent("today's date")[0], "DATE")
        
    def test_web_search(self):
        self.assertEqual(parse_intent("Search for python tutorials")[0], "WEB_SEARCH")
        self.assertEqual(parse_intent("look up the latest news")[0], "WEB_SEARCH")
        self.assertEqual(parse_intent("google how to tie a tie")[0], "WEB_SEARCH")
        
    def test_extract_search_query(self):
        self.assertEqual(extract_search_query("search for python tutorials"), "python tutorials")
        self.assertEqual(extract_search_query("google how to tie a tie"), "how to tie a tie")
        
    def test_exit(self):
        self.assertEqual(parse_intent("Stop listening")[0], "EXIT")
        self.assertEqual(parse_intent("Goodbye")[0], "EXIT")
        
    def test_unknown(self):
        self.assertEqual(parse_intent("Dance for me")[0], "UNKNOWN")
        self.assertEqual(parse_intent("")[0], "UNKNOWN")

if __name__ == '__main__':
    unittest.main()
