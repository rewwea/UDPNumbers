import socket

SERVER_IP = "0.0.0.0"
SERVER_PORT = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP, SERVER_PORT))

print(f"UDP сервер запущен на порту {SERVER_PORT}")

while True:
    data, addr = sock.recvfrom(1024)
    number = data.decode()
    print(f"Получено число: {number} от {addr}")