from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from Source.Domain.InterfaceAnalyseur import AnalyseurTexte
from Source.Domain.Langue.LanguesSupportees import Francais, Anglais
from Source.Infrastructure.HorlogeSysteme import HorlogeSysteme
import json


class RequetesHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        langue = self.headers.get('Accept-Language', 'fr')
        horloge = HorlogeSysteme()
        salutation = self._choisir_langue(langue).saluer(horloge.heure_actuelle())

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(salutation.encode('utf-8'))

    def do_POST(self):
        contenu_longueur = int(self.headers['Content-Length'])
        contenu = self.rfile.read(contenu_longueur).decode('utf-8')
        data = json.loads(contenu)

        texte = data.get('texte', '')
        langue = data.get('langue', 'fr')

        horloge = HorlogeSysteme()
        analyser = AnalyseurTexte(self._choisir_langue(langue), horloge)
        resultat = analyser.analyser_chaine(texte)

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        response_data = {
            'texte_inverse': resultat,
        }
        self.wfile.write(json.dumps(response_data).encode('utf-8'))

    def _choisir_langue(self, langue):
        if langue == 'fr':
            return Francais()
        elif langue == 'en':
            return Anglais()
        else:
            return Francais()  # Utilisation de Français par défaut


def main():
    port = 8000
    serveur = HTTPServer(('localhost', port), RequetesHandler)
    print(f'Serveur démarré sur le port {port}')
    serveur.serve_forever()


if __name__ == "__main__":
    main()