import socket
import json

sock = socket.socket()
sock.connect(('localhost', 9090))
a, b = map(int, input("Введите верхнюю и нижнюю сторону трапеции черех пробел: ").split(' '))
h = int(input("Введите высоту трапеции: "))
sock.send(json.dumps([a, b, h]).encode())

data = json.loads(sock.recv(1024).decode())
sock.close()

print("Площадь трапеции равна", data[0])

