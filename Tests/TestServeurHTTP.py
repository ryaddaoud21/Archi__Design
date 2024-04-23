import threading
import unittest
import datetime
from http.server import HTTPServer
from http.client import HTTPConnection
import json

from Source.Application.HTTP.serveur_http import RequetesHandler
from Source.Domain.Langue.LanguesSupportees import Francais, Anglais

class TestRequetesHandler(unittest.TestCase):
    def setUp(self):
        self.server_address = ('localhost', 8000)
        self.server = HTTPServer(self.server_address, RequetesHandler)
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.daemon = True
        self.server_thread.start()

    def test_do_GET(self):
        conn = HTTPConnection(*self.server_address)
        conn.request("GET", "/")
        response = conn.getresponse()

        self.assertEqual(response.status, 200)
        self.assertEqual(response.headers['Content-type'], 'text/html')

        # Vérification du contenu de la réponse
        expected_salutation = Francais().saluer(datetime.datetime.now().hour).encode('utf-8')
        self.assertEqual(response.read(), expected_salutation)

    def test_do_POST(self):
        conn = HTTPConnection(*self.server_address)
        data = json.dumps({'texte': 'radar', 'langue': 'fr'})
        headers = {'Content-type': 'application/json'}
        conn.request("POST", "/", data, headers)
        response = conn.getresponse()

        self.assertEqual(response.status, 200)
        self.assertEqual(response.headers['Content-type'], 'application/json')

        # Vérification du contenu de la réponse
        response_data = json.loads(response.read().decode('utf-8'))
        self.assertIn('texte_inverse', response_data)
        self.assertEqual(response_data['texte_inverse'], 'radar  Bien dit !')  # Vérifiez la valeur attendue du texte inversé

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()

if __name__ == '__main__':
    unittest.main()
