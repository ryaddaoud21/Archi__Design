import unittest
from Domain.services import Francais, AnalyseurTexte
from Infrastructure.HorlogeSysteme import HorlogeSysteme
class TestAnalyseurTexte(unittest.TestCase):
    def setUp(self):
        self.langue = Francais()
        self.horloge = HorlogeSysteme()

    def test_analyser_chaine_palindrome(self):
        texte_palindrome = "radar"
        analyseur = AnalyseurTexte(self.langue, self.horloge)
        resultat = analyseur.analyser_chaine(texte_palindrome)
        self.assertEqual(resultat, f"{texte_palindrome}  {self.langue.feliciter()}")

    def test_analyser_chaine_non_palindrome(self):
        texte_non_palindrome = "hello"
        analyseur = AnalyseurTexte(self.langue, self.horloge)
        resultat = analyseur.analyser_chaine(texte_non_palindrome)
        self.assertEqual(resultat, texte_non_palindrome[::-1])

if __name__ == "__main__":
    unittest.main()
