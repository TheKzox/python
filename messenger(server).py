import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('127.0.0.1', 12124))
    s.listen()
    while True:
        connection, address = s.accept()
        with connection:
            print(f'connected to {address}.')
            while True:
                data = connection.recv(1024)
                if not data:
                    break
                print(data.decode())
                message = f'User2: {input('enter your message: ')}'
                if message == 0:
                    break
                connection.sendall(message.encode())
