import socket
import json

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

print('connected:', addr)

while True:
    data = conn.recv(2048)
    if not data:
        break
    data = json.loads(data.decode())
    square = ((data[0] + data[1]) / 2) * data[2]
    conn.send(json.dumps([square]).encode())

conn.close()

