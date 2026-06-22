#!/usr/bin/env python3
"""Local server for CEO Builder — serves static files + persists state to state.json."""
import json, os, sys
from http.server import HTTPServer, SimpleHTTPRequestHandler

STATE_FILE = os.path.join(os.path.dirname(__file__), 'state.json')
PORT = 4200

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.path.dirname(__file__), **kwargs)

    def do_GET(self):
        if self.path == '/api/state':
            self._send_state()
        else:
            super().do_GET()

    def do_POST(self):
        if self.path == '/api/state':
            length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(length)
            try:
                data = json.loads(body)
                with open(STATE_FILE, 'w') as f:
                    json.dump(data, f)
                self._json(200, {'ok': True})
            except Exception as e:
                self._json(500, {'error': str(e)})
        else:
            self.send_error(404)

    def do_OPTIONS(self):
        self.send_response(200)
        self._cors()
        self.end_headers()

    def _send_state(self):
        if os.path.exists(STATE_FILE):
            with open(STATE_FILE) as f:
                raw = f.read()
            self.send_response(200)
            self._cors()
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(raw.encode())
        else:
            self._json(404, {'error': 'no state yet'})

    def _json(self, code, obj):
        body = json.dumps(obj).encode()
        self.send_response(code)
        self._cors()
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', len(body))
        self.end_headers()
        self.wfile.write(body)

    def _cors(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')

    def log_message(self, fmt, *args):
        # suppress noisy access logs, only show errors
        if args and str(args[1]) not in ('200', '304'):
            super().log_message(fmt, *args)

if __name__ == '__main__':
    httpd = HTTPServer(('', PORT), Handler)
    print(f'CEO Builder running at http://localhost:{PORT}/tracker.html')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\nStopped.')
