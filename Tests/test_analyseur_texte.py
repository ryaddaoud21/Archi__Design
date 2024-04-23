import unittest
from Source.Infrastructure.HorlogeSysteme import HorlogeSysteme
from Source.Domain.InterfaceAnalyseur import AnalyseurTexte
from Source.Domain.Langue.Langue import Francais

class TestAnalyseurTexte(unittest.TestCase):
    def test_palindrome_detection(self):
        langue = Francais()
        horloge = HorlogeSysteme()
        analyseur = AnalyseurTexte(langue, horloge)
        self.assertEqual(analyseur.analyser_chaine("radar"), "radar  Bien dit !")
        self.assertEqual(analyseur.analyser_chaine("hello"), "olleh")

if __name__ == '__main__':
    unittest.main()
