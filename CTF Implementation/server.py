from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

keylog = """CLIENT_HANDSHAKE_TRAFFIC_SECRET b6e12e5dc6751dccc9435be608e4cfc5490fd9e0fd3ebfac5f1d313903ad570c fefc15fcee22e2bad362b4e2305ef4383c3069ad42ce8c92b90edc558cb3c68fc09735e986a5e08d567374fbc6453482
SERVER_HANDSHAKE_TRAFFIC_SECRET b6e12e5dc6751dccc9435be608e4cfc5490fd9e0fd3ebfac5f1d313903ad570c 06fa0c09f15cc73b414b969aeafb365550fbbf81e31f86e7c56af5fdab46180dc29e0618125bc856bbfe906d5556d7a7
CLIENT_TRAFFIC_SECRET_0 b6e12e5dc6751dccc9435be608e4cfc5490fd9e0fd3ebfac5f1d313903ad570c 75dbe1a1ac4767eabc64cbeebb7d7d534b92a9e8a87c3f601b196c072dd144337e0bf52215fd82f837cb4768a663c9f8
SERVER_TRAFFIC_SECRET_0 b6e12e5dc6751dccc9435be608e4cfc5490fd9e0fd3ebfac5f1d313903ad570c 4c91e73b9a45d819b211c872d914127aac5591f8f892f34de1377561335d7b68658b71f09d961f8b095349fd7047b67f
EXPORTER_SECRET b6e12e5dc6751dccc9435be608e4cfc5490fd9e0fd3ebfac5f1d313903ad570c 9c8880d7ba7c26afb79f345dcf1fe9af6cd56c5af9ebd92dde61015c7f48ec779de2c47e7e919ad4d2f2c57f2f08399c
"""

clue = "BLM and FEM! - File Extensions Matters!"

def log_message(self, format, *args):
    # Suppress the logging by overriding this method and not printing anything
    pass

def log_request(self, code='-', size='-'):
    # Suppress the request logging by overriding this method and not printing anything
    pass

# Custom request handler
class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/keylogfile.log':
            # Send response status code
            self.send_response(200)
            # Send headers
            self.send_header("Content-type", "text/plain")
            self.end_headers()

            # Send the keylog content
            self.wfile.write(keylog.encode('utf-8'))
            httpd.shutdown()

            
        else:
            # Send response status code
            self.send_response(200)
            # Send headers
            self.send_header("Content-type", "text/plain")
            self.end_headers()

            # Send the clue
            self.wfile.write(clue.encode('utf-8'))

# Define the server address and port
server_address = ('', 1947)  # port 1947

# Create the HTTP server using ThreadingHTTPServer
httpd = ThreadingHTTPServer(server_address, CustomHandler)

# Start the server
print("CIA Secret Key Server is running on the secret port!\nYou can ask for any file you may need...")
httpd.serve_forever()
