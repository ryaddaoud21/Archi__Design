import unittest
from Domain.services import  AnalyseurTexte, Francais
from Infrastructure.HorlogeSysteme import HorlogeSysteme


class TestAnalyseurTexte(unittest.TestCase):
    def test_palindrome_detection(self):
        langue = Francais()
        horloge = HorlogeSysteme()
        analyseur = AnalyseurTexte(langue, horloge)
        self.assertTrue(analyseur.est_palindrome("radar"))
        self.assertFalse(analyseur.est_palindrome("hello"))

if __name__ == '__main__':
    unittest.main()
