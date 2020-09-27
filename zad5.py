from pymodbus.client.sync import ModbusTcpClient
import http.server
import socketserver

address = 200 
value = 1
unitId = 1
host = "127.0.0.1"
PORT = 5020
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    client = ModbusTcpClient(host, PORT)
    client.connect()
    client.write_register(address,value,unit=unitId)
    httpd.serve_forever()

.put("/api/open")
    def funcname(parameter_list):
        """
        docstring
        """
        pass
