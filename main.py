from http.server import HTTPServer
from server import ScanmeServer

HOSTNAME = "127.0.0.1"
PORT = 8080

if __name__ == '__main__':
    HTTPServer((HOSTNAME, PORT), ScanmeServer).serve_forever()
    # print("Server Starts - %s:%s" % (HOSTNAME, PORT))
