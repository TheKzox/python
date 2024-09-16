import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('127.0.0.1', 12124))
    while True:
        message = f'User1: {input('enter your message: ')}'
        s.sendall(message.encode())
        data = s.recv(1024)
        print(data.decode())
