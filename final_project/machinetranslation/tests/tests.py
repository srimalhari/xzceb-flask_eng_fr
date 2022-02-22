"""This is the testing python file. It tests the two functions
in translator.py pyhton file"""
import unittest

from translator import english_to_french, french_to_english

class TestFrenchTranslator(unittest.TestCase):
    """This is the test class. It has a function to test the translator.py
    english_to_french functions"""

    def test_englist_to_french(self):
        """Test the english_to_french function with 2 values"""
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('None'), '')

class TestEnglishTranslator(unittest.TestCase):
    """This is the test class. It has a function to test the translator.py
    french_to_english functions"""

    def test_french_to_english(self):
        """Test the french_to_english function with 2 values"""
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('None'), '')

unittest.main()