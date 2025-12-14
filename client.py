import socket
import time

SERVER_IP = "127.0.0.1"  # адрес сервера
SERVER_PORT = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for i in range(1, 11):
    message = str(i)
    sock.sendto(message.encode(), (SERVER_IP, SERVER_PORT))
    time.sleep(1)

sock.close()