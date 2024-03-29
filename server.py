import http.server, os, sys

BaseHandler = http.server.BaseHTTPRequestHandler

tvitovi = []

class Handler(BaseHandler):
        
    def _set_headers(self, type):
        self.send_response(200)
        self.send_header('Content-type', type)
        self.end_headers()

    def do_GET(self):
        filename = self.path.split("/")[-1]
        if filename == "" :
            filename = "index.html"
        extension = filename.split(".")[-1]
        if os.access(filename, os.R_OK) and not os.path.isdir(filename):
            ext = filename.split(".")[-1]
            mode = "r"
            if ext in ["html","htm"]:
                content_type = "text/html"
            elif ext in ["txt","js","py","php"]:
                content_type = "text/plain"
            elif ext in ["css"]:
                content_type = "text/css"
            elif ext in ["ico","jpg","jpeg","png","gif"]:
                content_type = "image/x-icon"
                mode = "rb"
            file = open(filename, mode)
            content = file.read()
            if mode == "r":
                content = str.encode(content)
            file.close()
            try:
                self._set_headers(content_type)
                self.wfile.write(content)
            except:
                print("problem sa serverom")        
        else:
            #odgovor = {"metod":"GET", "path": self.path, "sadrzaj": ""}
            #self._set_headers("text/json")
            self.wfile.write(str.encode(str("Not found")))
            
    def do_POST(self):
        duzina_sadrzaja = int(self.headers['Content-Length'])
        sadrzaj = self.rfile.read(duzina_sadrzaja).decode("utf-8")
        if eval(sadrzaj)["tvit"] != "":
            tvitovi.append(sadrzaj)
        self._set_headers("text/plain")
        self.wfile.write(str.encode(str(tvitovi)))
try:
    port = int(os.environ["PORT"])
    print("port: ",port)
    #httpd = http.server.HTTPServer(('0.0.0.0', port), Handler)
    httpd = http.server.HTTPServer(('', port), Handler)
    print("Server startovan...port: ",port)
    httpd.serve_forever()
except:
    print("Server stopiran")
