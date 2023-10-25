# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
from channelSwitcher import switcher as swt
from bottle import template

hostName = '192.168.35.10'
serverPort = 8000

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
            path = self.path
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            res = swt(path)    #send the path of the request to swt and get res
            if res == 'QUIT':
                webServer.server_close()
            self.wfile.write(bytes(template('index', path=self.path), 'utf-8'))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")