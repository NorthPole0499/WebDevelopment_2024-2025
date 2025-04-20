import socket
import json
import webbrowser
import os

sock = socket.socket()
sock.connect(('localhost', 9090))
sock.send(b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")

data = sock.recv(4096).decode('utf-8')

with open('index_new.html', 'w', encoding='utf-8') as file:
    file.write(data)

webbrowser.open('file://' + os.path.realpath('index_new.html'))

sock.close()
