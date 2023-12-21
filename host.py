import socket
import socketserver
import requests

class ProxyRequestHandler(socketserver.StreamRequestHandler):
    def handle(self):
        # Receive the request from the client
        request_data = self.rfile.readall()

        # Parse the request data into a request object
        request = requests.Request()
        request.parse_raw(request_data)

        # Modify the request headers to hide the hostname
        request.headers['Host'] = 'localhost'

        # Send the modified request to the target URL
        response = requests.request(request.method, request.url, headers=request.headers, data=request.body)

        # Send the response back to the client
        self.wfile.write(response.content)

# Create and start the proxy server
with socketserver.TCPServer(('', 80), ProxyRequestHandler) as server:
    server.serve_forever()