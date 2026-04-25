from http.server import BaseHTTPRequestHandler, HTTPServer
import json

PORT = 9000

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/user/list":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            data = {
                "users": [
                    {"name": "Alice", "password": "alice123"},
                    {"name": "Bob", "password": "bob123"}
                ]
            }

            self.wfile.write(json.dumps(data).encode())
        else:
            self.send_response(404)
            self.end_headers()

HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()