from http.server import BaseHTTPRequestHandler
from utils import add
import sma

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('Hello, world!'.encode('utf-8'))
        print("hello")
        result = add(3,2)
        print(result)
        return
