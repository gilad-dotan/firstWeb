from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
serverPort = 8080

DEFAULT_PAGE = "mainPage.html"

class MyServer(BaseHTTPRequestHandler):

    def loadPage(self, path):
        content = ""
        path = path[1:]

        if path == "":
            path = DEFAULT_PAGE

        print("--- " + path + " ---")
        try:
            with open(path, "r") as file:
                content = file.readlines()

            for i in content:
                self.wfile.write(bytes(i, "utf-8"))
        except:
            pass

    def do_POST(self):
        '''Reads post request body'''
        content_len = int(self.headers.getheader('content-length', 0))
        post_body = self.rfile.read(content_len)
        self.wfile.write("received post request:<br>{}".format(post_body))
        print(post_body)

    def do_GET(self):

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.loadPage(self.path)

        #self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        #self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        #self.wfile.write(bytes("<body>", "utf-8"))
        #self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        #self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")