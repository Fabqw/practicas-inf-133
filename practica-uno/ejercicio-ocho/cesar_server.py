from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from urllib import parse as urlparse

# Aplicando los principios de desarrollo de Software DRY, KISS, YAGNI y 
# la S de SOLID construye una API RESTful para encriptar mensajes, la API debe permitir:
mensajes = []

class HTTPResponseHandler:
    @staticmethod
    def handle_response(handler, status, data):
        handler.send_response(status)
        handler.send_header("Content-type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(data).encode("utf-8"))

    @staticmethod
    def handle_reader(handler):
        content_length = int(handler.headers["Content-Length"])
        post_data = handler.rfile.read(content_length)
        return json.loads(post_data.decode("utf-8"))

class MensajeService:
    @staticmethod
    def mensaje_cifrado(mensaje):
        mensaje = mensaje.lower()
        new_mensaje = ""
        for char in mensaje:
            if char.isalpha():
                ascii_code = ord(char)
                ascii_code = (ascii_code - 97 + 3) % 26 + 97
                new_mensaje += chr(ascii_code)
            else:
                new_mensaje += char
        return new_mensaje
        



        
    



# Crear un mensaje
# Listar todos los mensajes
# Buscar mensajes por ID
# Actualizar el contenido de un mensaje
# Eliminar un mensaje
# De los mensajes se debe almacenar la siguiente información:

# ID (identificador único)
# Contenido (mensaje a encriptar)
# Contenido encriptado

# El encriptado debe ser realizado con el algoritmo de cifrado César, 
# donde cada letra del mensaje debe ser reemplazada por la letra que se encuentra 3 posiciones adelante en el alfabeto. Por ejemplo, la letra a debe ser reemplazada por la letra d, la letra b por la letra e, y así sucesivamente.

# Sugerencia: Utiliza los ASCII codes para realizar el encriptado.