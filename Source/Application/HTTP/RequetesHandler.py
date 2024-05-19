from http.server import BaseHTTPRequestHandler
from Source.Domain.InterfaceAnalyseur import AnalyseurTexte
from Source.Langue.FabriqueLangue import FabriqueLangue
from Source.Infrastructure.HorlogeSysteme import HorlogeSysteme
import json

class RequetesHandler(BaseHTTPRequestHandler):
    def _choose_language(self, language):
        try:
            return FabriqueLangue.create_language(language)
        except KeyError:
            self.send_error(400, "Langue non supportée.")
            return None

    def _process_get_request(self):
        try:
            language = self.headers.get('Accept-Language', 'fr')
            clock = HorlogeSysteme()
            language_instance = self._choose_language(language)
            if language_instance is None:
                return
            greeting = language_instance.saluer(clock.heure_actuelle())

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(greeting.encode('utf-8'))
        except Exception as e:
            self.send_error(500, f"Erreur interne du serveur: {str(e)}")

    def _process_post_request(self):
        try:
            content_length = int(self.headers['Content-Length'])
            content = self.rfile.read(content_length).decode('utf-8')
            data = json.loads(content)

            text = data.get('texte', '')
            language = data.get('langue', 'fr')

            clock = HorlogeSysteme()
            language_instance = self._choose_language(language)
            if language_instance is None:
                return
            analyzer = AnalyseurTexte(language_instance, clock)
            result = analyzer.analyser_chaine(text)

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            response_data = {'texte_inverse': result}
            self.wfile.write(json.dumps(response_data).encode('utf-8'))
        except json.JSONDecodeError:
            self.send_error(400, "JSON mal formé.")
        except KeyError as e:
            self.send_error(400, f"Donnée manquante: {str(e)}")
        except Exception as e:
            self.send_error(500, f"Erreur interne du serveur: {str(e)}")

    def do_GET(self):
        self._process_get_request()

    def do_POST(self):
        self._process_post_request()
