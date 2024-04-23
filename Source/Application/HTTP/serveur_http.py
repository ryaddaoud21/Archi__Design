from http.server import BaseHTTPRequestHandler, HTTPServer
from Source.Domain.InterfaceAnalyseur import AnalyseurTexte
from Source.Domain.Langue.LanguesSupportees import Anglais,Francais
from Source.Infrastructure.HorlogeSysteme import HorlogeSysteme



class RequetesHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<html><body><h1>GET request received!</h1></body></html>")

    def do_POST(self):
        contenu_longueur = int(self.headers['Content-Length'])
        contenu = self.rfile.read(contenu_longueur).decode('utf-8')
        langue = self.headers.get('Accept-Language', 'fr')
        horloge = HorlogeSysteme()
        analyser = AnalyseurTexte(self._choisir_langue(langue), horloge)
        resultat = analyser.analyser_chaine(contenu)

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(resultat.encode('utf-8'))

    def _choisir_langue(self, langue):
        if langue.startswith('fr'):
            return Francais()
        elif langue.startswith('en'):
            return Anglais()
        else:
            return Francais()  # Utilisation de Français par défaut


def main():
    port = 8000
    serveur = HTTPServer(('', port), RequetesHandler)
    print(f'Serveur démarré sur le port {port}')
    serveur.serve_forever()


if __name__ == "__main__":
    main()
