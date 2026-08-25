import unittest
from src.reminder import parse_duration

class TestReminderParser(unittest.TestCase):
    
    def test_seconds(self):
        self.assertEqual(parse_duration("remind me in 10 seconds"), 10)
        self.assertEqual(parse_duration("set a reminder for 5 secs"), 5)
        
    def test_minutes(self):
        self.assertEqual(parse_duration("remind me in 1 minute"), 60)
        self.assertEqual(parse_duration("set an alarm for 5 minutes"), 300)
        
    def test_hours(self):
        self.assertEqual(parse_duration("remind me in 1 hour"), 3600)
        self.assertEqual(parse_duration("set a timer for 2 hrs"), 7200)
        
    def test_combined(self):
        self.assertEqual(parse_duration("remind me in 1 hour and 30 minutes"), 5400)
        self.assertEqual(parse_duration("set a timer for 2 minutes and 15 seconds"), 135)
        
    def test_invalid(self):
        self.assertEqual(parse_duration("remind me soon"), 0)
        self.assertEqual(parse_duration("set a reminder for tomorrow"), 0)
        self.assertEqual(parse_duration(""), 0)

if __name__ == '__main__':
    unittest.main()
