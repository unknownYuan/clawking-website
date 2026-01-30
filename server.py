#!/usr/bin/env python3
"""Simple HTTP server for ClawKing website"""

import http.server
import socketserver
import os

PORT = 8080
DIRECTORY = os.path.dirname(__file__) or '.'

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

print(f"🦞 ClawKing Website Server")
print(f"📍 Running at: http://localhost:{PORT}")
print(f"🌐 Open in your browser!")
print(f"\nPress Ctrl+C to stop\n")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
