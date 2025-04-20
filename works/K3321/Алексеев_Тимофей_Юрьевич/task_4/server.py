import socket
import threading


def find_name(conn):
    for elem in clients:
        if elem[0] == conn:
            return elem[1]


def send_all_clients(message, sender):
    for client in clients:
        if client[0] != sender:
            print(client)
            try:
                client[0].send(message)
            except Exception:
                delete_client(client)


def delete_client(client):
    if client in clients:
        name = client[1]
        send_all_clients(f"{name} вышел из чата".encode('utf-8'), client[0])
        clients.remove(client)
        client[0].close()


def handle_client(conn):
    while True:
        try:
            message = conn.recv(1024)
            print(message)
            if message:
                current_name = find_name(conn)
                send_all_clients(f"{current_name}: {message.decode('utf-8')}".encode('utf-8'), conn)
            else:
                delete_client((conn, find_name(conn)))
                break
        except Exception as e:
            print('Ошибка:', e)
            delete_client((conn, find_name(conn)))
            break


clients = []

sock = socket.socket()
sock.bind(('localhost', 9090))
sock.listen()


while True:
    conn, addr = sock.accept()

    conn.send("name".encode('utf-8'))
    client_name = conn.recv(1024).decode('utf-8')

    clients.append((conn, client_name))

    send_all_clients(f"{client_name} вошёл в чат".encode('utf-8'), conn)
    # conn.send("Вы подключились к серверу".encode('utf-8'))

    thread = threading.Thread(target=handle_client, args=(conn,))
    thread.start()

conn.close()