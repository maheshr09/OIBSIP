import unittest
from src.knowledge import fetch_answer, clean_query

class TestKnowledgeBase(unittest.TestCase):
    
    def test_clean_query(self):
        self.assertEqual(clean_query("What is python?"), "python?")
        self.assertEqual(clean_query("tell me about open source"), "open source")
        self.assertEqual(clean_query("who is the creator of python"), "the creator of python")
        
    def test_fetch_answer_success(self):
        # Should match regardless of casing or surrounding punctuation
        self.assertIsNotNone(fetch_answer("python?"))
        self.assertIsNotNone(fetch_answer("tell me about the speed of light"))
        self.assertEqual(fetch_answer("capital of india"), "The capital of India is New Delhi.")
        
    def test_fetch_answer_not_found(self):
        self.assertIsNone(fetch_answer("the meaning of life"))
        self.assertIsNone(fetch_answer("something completely random"))
        self.assertIsNone(fetch_answer(""))

if __name__ == '__main__':
    unittest.main()
