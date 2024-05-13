import json
import os
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer


class EnvironmentHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self) -> None:
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({**os.environ}).encode("UTF-8"))


httpd = HTTPServer(('0.0.0.0', 7777), EnvironmentHTTPRequestHandler)

if __name__ == "__main__":
    httpd.serve_forever()
