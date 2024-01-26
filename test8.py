

from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        if self.path == "/hi":
            self.wfile.write(bytes("<p>Hello there</p>", "utf-8"))
            

        if self.path == "/99":
            line = ""
            for i in range(2, 10):
                for j in range(1,10):
                    line += (f"{i} * {j} = {i*j}<br>\n")
                line += "<br>\n"
            self.wfile.write(bytes("<p>" + line + "<p>", "utf-8"))
            print(line)
        
        self.wfile.write(bytes("</body></html>", "utf-8"))




if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")