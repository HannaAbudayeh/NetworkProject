import socket
import os
import time

HOST = "192.168.1.150"
PORT = 9955

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connectionName = "1200640"

    try:
        client.connect((HOST, PORT))
        client.sendall(bytes(connectionName, "utf-8"))
        response = client.recv(1024)
        print(response.decode())
        time.sleep(10)
        os.system("rundll32.exe user32.dll,LockWorkStation")

    finally:
        client.close()

while True:
    main()