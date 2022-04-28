import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test_english_to_french(self): 
        self.assertEqual(english_to_french(""), "") 
        self.assertEqual(english_to_french("Hello"), "Bonjour")   

class TestFrenchToEnglis(unittest.TestCase): 
    def test_french_to_english(self): 
        self.assertEqual(french_to_english(""), "") 
        self.assertEqual(french_to_english("Bonjour"), "Hello")

unittest.main()