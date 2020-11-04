from http import cookies
from http.server import BaseHTTPRequestHandler, HTTPServer

class TestRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(self.headers)
        cks = cookies.SimpleCookie(self.headers.get('Cookie'))
        print(cks)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(str.encode(str(cks)))

def run():
    server_address = ("", 8080)
    httpd = HTTPServer(server_address, TestRequestHandler)
    httpd.serve_forever()

if __name__ == "__main__":
    run()
