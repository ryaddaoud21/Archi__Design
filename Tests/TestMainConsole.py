import unittest
from unittest.mock import patch
from Application.main_console import main

class TestMainConsole(unittest.TestCase):
    def test_greeting(self):
        console = main()
        with patch('builtins.input', return_value='fr'):
            self.assertEqual(console.greet(), "Bonjour")
        with patch('builtins.input', return_value='en'):
            self.assertEqual(console.greet(), "Good morning")

    def test_farewell(self):
        console = main()
        with patch('builtins.input', return_value='fr'):
            self.assertEqual(console.say_goodbye(), "Au revoir")
        with patch('builtins.input', return_value='en'):
            self.assertEqual(console.say_goodbye(), "Goodbye")

if __name__ == '__main__':
    unittest.main()
