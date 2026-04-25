from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess
import urllib.parse
import requests

PORT = 3000

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path.startswith("/search"):
            self.handle_search()
        elif self.path.startswith("/joke"):
            self.handle_joke()
        elif self.path.startswith("/login"):
            self.handle_login()
        else:
            self.serve_index()

    # -----------------------
    # Frontend UI
    # -----------------------
    def serve_index(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()

        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Security Demo</title>
            <style>
                body {
                    font-family: Arial;
                    background: #0f172a;
                    color: white;
                    text-align: center;
                    padding: 40px;
                }
                h1 {
                    font-size: 40px;
                }
                .card {
                    background: #1e293b;
                    padding: 20px;
                    margin: 20px auto;
                    width: 60%;
                    border-radius: 10px;
                }
                button {
                    padding: 10px 20px;
                    margin: 5px;
                    border: none;
                    border-radius: 5px;
                    background: #3b82f6;
                    color: white;
                    cursor: pointer;
                }
                p {
                    margin-top: 15px;
                }
            </style>
        </head>
        <body>

            <h1>🚀 Demo Website</h1>

            <div class="card">
                <h2>😂 Random Joke</h2>
                <button onclick="getJoke()">Get Joke</button>
                <p id="joke"></p>
            </div>

            <div class="card">
                <h2>🔐 Login</h2>
                <button onclick="login()">Login</button>
                <p id="loginResult"></p>
            </div>

            <script>
                async function getJoke() {
                    const res = await fetch("/joke");
                    const data = await res.json();
                    document.getElementById("joke").innerText = data.joke;
                }

                async function login() {
                    const res = await fetch("/login");
                    const data = await res.json();
                    document.getElementById("loginResult").innerText = data.message;
                }
            </script>

        </body>
        </html>
        """

        self.wfile.write(html.encode("utf-8"))

    # -----------------------
    # Backend proxy
    # -----------------------
    def handle_joke(self):
        try:
            res = requests.get("http://backend:5000/message")
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(res.content)
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(str(e).encode())

    # -----------------------
    # ClientAPI proxy
    # -----------------------
    def handle_login(self):
        try:
            res = requests.get("http://clientapi:8000/login")
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(res.content)
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(str(e).encode())

    # -----------------------
    # Simulated RCE endpoint
    # -----------------------
    def handle_search(self):
        query = urllib.parse.urlparse(self.path).query
        params = urllib.parse.parse_qs(query)
        user_input = params.get("input", [""])[0]

        if not user_input:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Usage: /search?input=<command>\n")
            return

        try:
            # ⚠️ Intentional vulnerability for demo
            result = subprocess.check_output(
                user_input,
                shell=True,
                stderr=subprocess.STDOUT
            )

            self.send_response(200)
            self.end_headers()
            self.wfile.write(result)

        except subprocess.CalledProcessError as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(e.output)


HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()