import socket
import time

print("Host iniciado!")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", 5000))

while True:
    dados, addr = sock.recvfrom(1024)
    print(f"[RECEBIDO] De {addr}: {dados.decode()}")
    time.sleep(1)