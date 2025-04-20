import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

print('connected:', addr)

while True:
    data = conn.recv(2048)
    if not data:
        break
    print(data)
    if data == b'Hello, server!':
        conn.send(b'Hello, client!')
    else:
        conn.send(b'Error')

conn.close()

