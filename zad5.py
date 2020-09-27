from pymodbus.client.sync import ModbusTcpClient
from fastapi import FastAPI, Response, status

app = FastAPI()

@app.post("/api/open", status_code=200)
def open(response: Response):
    try:
        client = ModbusTcpClient(host='192.168.1.15', port='5020')
        client.connect()
        client.write_registers(200, 1)
    except:
        response.status_code = status.HTTP_404_NOT_FOUND
        return{"status":"Door closed"}
    return {"status":"Door opened"}


