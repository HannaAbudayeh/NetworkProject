import socket
import time

HOST = "192.168.1.150"
PORT = 9955

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print("Server is running...")

    conn, address = server.accept()
    print("Connection from", address)

    data = conn.recv(1024)
    connectionName = data.decode()
    print("Received message from", connectionName)

    if connectionName in ["1200640", "1193102", "1200085"]:
        conn.sendall(b"The screen will lock in 10 seconds")
        time.sleep(10)
        print("The screen is locked")
    else:
        conn.sendall(b"Invalid connection name")

    conn.close()

if __name__ == "__main__":
    main()