from http.server import HTTPServer
from Source.Application.HTTP.RequetesHandler import RequetesHandler
from Source.Application.HTTP.Configuration import SERVER_PORT,SERVER_HOST


def main():
    port = SERVER_PORT
    server_address = (SERVER_HOST, port)

    try:
        server = HTTPServer(server_address, RequetesHandler)
        print(f'Serveur démarré sur le port {port}')
        server.serve_forever()
    except Exception as e:
        print(f"Erreur lors de l'exécution du serveur: {e}")
    finally:
        print("Arrêt du serveur.")
        server.server_close()


if __name__ == "__main__":
    main()
