import socket
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

from scan import validate_identity_card

HOSTNAME = "127.0.0.1"
PORT = 8080

class ScanmeServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.wfile.write(bytes("Poshel naher\n", "utf-8"))

    def do_POST(self):
        if not 'Content-Length' in self.headers:
            self.send_response(400)
            return

        content_length = int(self.headers['Content-Length'])
        raw_data = self.rfile.read(content_length)
        data = json.loads(raw_data.decode('utf-8'))

        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

        is_valid = validate_identity_card(data['user_info'], data['ic_image_uri'])
        print('Validatation result', is_valid)

        if is_valid:
            self.wfile.write(bytes('{\"is_valid\": true}\n', "utf-8"))
        else:
            self.wfile.write(bytes('{\"is_valid\": false}\n', "utf-8"))

