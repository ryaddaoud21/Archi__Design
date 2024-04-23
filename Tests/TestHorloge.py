import unittest
from Source.Infrastructure.HorlogeSysteme import HorlogeSysteme

class TestHorloge(unittest.TestCase):
    def test_time(self):
        horloge = HorlogeSysteme()
        self.assertIsNotNone(horloge.heure_actuelle())

if __name__ == '__main__':
    unittest.main()
