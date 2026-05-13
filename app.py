import os
from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("Application deployee sur Render sans Flask 🚀")

port = int(os.environ.get("PORT", 10000))  # Render fournit PORT

server = HTTPServer(("0.0.0.0", port), Handler)

print(f"Server running on port {port}")
server.serve_forever()