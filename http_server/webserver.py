https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
import SimpleHTTPServer
import SocketServer

class CS144Handler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    # Disable logging DNS lookups
    def address_string(self):
        return str(self.client_address[0])


PORT = 80

Handler = CS144Handler
httpd = SocketServer.TCPServer(("", PORT), Handler)
print "httpd serving at port", PORT
httpd.serve_forever()
