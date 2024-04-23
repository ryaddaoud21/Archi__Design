import unittest
from Source.Infrastructure.HorlogeSysteme import HorlogeSysteme
from Source.Domain.InterfaceAnalyseur import AnalyseurTexte
from Source.Domain.Langue import Francais

class TestAnalyseurTexte(unittest.TestCase):
    def test_palindrome_detection(self):
        langue = Francais()
        horloge = HorlogeSysteme()
        analyseur = AnalyseurTexte(langue, horloge)
        self.assertTrue(analyseur.analyser_chaine("radar"))
        self.assertFalse(analyseur.analyser_chaine("hello"))

if __name__ == '__main__':
    unittest.main()
