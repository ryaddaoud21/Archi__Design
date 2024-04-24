from http.server import HTTPServer
from Source.Application.HTTP.RequetesHandler import RequetesHandler
from Source.Application.HTTP.Configuration import SERVER_PORT,SERVER_HOST

def main():
    port = SERVER_PORT
    server_address = (SERVER_HOST, port)
    server = HTTPServer(server_address, RequetesHandler)
    print(f'Serveur démarré sur le port {port}')
    server.serve_forever()

if __name__ == "__main__":
    main()
