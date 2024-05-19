import unittest
from Source.Langue.LanguesSupportees import Anglais,Francais

class TestLangue(unittest.TestCase):
    def test_french_greeting(self):
        langue = Francais()
        self.assertEqual(langue.saluer(10), "Bonjour")

    def test_english_greeting(self):
        langue = Anglais()
        self.assertEqual(langue.saluer(10), "Good Morning")

if __name__ == '__main__':
    unittest.main()
