from http.server import BaseHTTPRequestHandler
from datetime import datetime
class handler(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/html')
    self.end_headers()
    self.wfile.write(<img-src="https://idsb.tmgrup.com.tr/ly/uploads/images/2020/10/20/66582.jpg"/).encode())
    return
