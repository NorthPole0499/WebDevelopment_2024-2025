import socket
import json

sock = socket.socket()
sock.bind(('localhost', 9090))
sock.listen(1)
conn, addr = sock.accept()

print('connected:', addr)

while True:
    with open('index.html', 'r', encoding='utf-8') as file:
        html_data = file.read()

    data = conn.recv(2048)
    if not data:
        break

    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/html; charset=utf-8\r\n"
        f"Content-Length: {len(html_data.encode('utf-8'))}\r\n"
        "Connection: close\r\n\r\n"
        f"{html_data}"
    )
    conn.send(response.encode('utf-8'))

conn.close()