import socket
import json
import webbrowser
import os
import threading


def receive_messages(conn):
    while True:
        try:
            message = conn.recv(1024).decode('utf-8')

            if message == "name":
                conn.send(name.encode('utf-8'))
            else:
                print(message, '\n')
        except Exception as e:
            print("Ошибка:", e)
            conn.close()
            break


def send_messages(conn):
    while True:
        message = input()
        if message.lower() == 'exit':
            conn.close()
            break
        print(f"{name}: {message}")
        conn.send(message.encode('utf-8'))


sock = socket.socket()
sock.connect(('localhost', 9090))

name = input('Введите ваше имя: ')

receive_thread = threading.Thread(target=receive_messages, args=(sock,))
receive_thread.start()

send_thread = threading.Thread(target=send_messages, args=(sock,))
send_thread.start()
