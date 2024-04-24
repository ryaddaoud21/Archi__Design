from http.server import BaseHTTPRequestHandler
from Source.Domain.InterfaceAnalyseur import AnalyseurTexte
from Source.Domain.Langue.FabriqueLangue import FabriqueLangue
from Source.Infrastructure.HorlogeSysteme import HorlogeSysteme
import json

class RequetesHandler(BaseHTTPRequestHandler):
    def _choose_language(self, language):
        return FabriqueLangue.create_language(language)

    def _process_get_request(self):
        language = self.headers.get('Accept-Language', 'fr')
        clock = HorlogeSysteme()
        greeting = self._choose_language(language).saluer(clock.heure_actuelle())

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(greeting.encode('utf-8'))

    def _process_post_request(self):
        content_length = int(self.headers['Content-Length'])
        content = self.rfile.read(content_length).decode('utf-8')
        data = json.loads(content)

        text = data.get('texte', '')
        language = data.get('langue', 'fr')

        clock = HorlogeSysteme()
        analyzer = AnalyseurTexte(self._choose_language(language), clock)
        result = analyzer.analyser_chaine(text)

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        response_data = {
            'texte_inverse': result
        }
        self.wfile.write(json.dumps(response_data).encode('utf-8'))

    def do_GET(self):
        self._process_get_request()

    def do_POST(self):
        self._process_post_request()


