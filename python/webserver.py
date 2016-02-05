from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from subprocess import call


from execShell import ExecApi;

execApi = ExecApi()

class webServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if( self.path.endswith("/exec") ):
                execApi.index(self);

        except IOError:
            server.send_error(404, 'File Not Found: %s' % server.path)


    def do_POST(self):
        if( self.path.endswith("/exec") ):
            execApi.execute(self)


def main():
    try:
        port = 666
        server = HTTPServer(('', port), webServerHandler)
        print ("Web Server running on port %s" % port)
        server.serve_forever()
    except KeyboardInterrupt:
        print (" ^C entered, stopping web server....")
        server.socket.close()

if __name__ == '__main__':
    main()
