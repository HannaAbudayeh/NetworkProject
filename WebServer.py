from socket import *

Websock = socket(AF_INET, SOCK_STREAM)
# Declare host name and its port
HOST_NAME = "192.168.1.108"
HOST_PORT = 9977

Websock.bind((HOST_NAME, HOST_PORT))
print("The server is ready!!\n")
Websock.listen(1)

while True:

    conn, addr = Websock.accept()
    sentence = conn.recv(1024).decode()
    ip = addr[0]
    port = addr[1]
    print(sentence)
    method, path, version = sentence.split()[0:3]

    if method == "GET":
        # صفحة الانجليزي
        if path in ["/","/en","/index.html","/main_en.html","/.html"]:
            conn.send("HTTP/1.1 200 OK\r\n".encode())
            conn.send("Content-Type: text/html\r\n".encode())
            conn.send("\r\n".encode())
            f1 = open("main_en.html","rb")
            conn.send(f1.read())
            f1.close()

        #صفحة العربية
        elif path in ["/ar", "/main_ar.html"]:
            conn.send("HTTP/1.1 200 OK\r\n".encode())
            conn.send("Content-Type: text/html\r\n".encode())
            conn.send("charset: utf-8\r\n".encode())
            conn.send("\r\n".encode())
            f1 = open("main_ar.html","rb")
            conn.send(f1.read())
            f1.close()

        #css file 
        elif path == "/.css":
            conn.send("HTTP/1.1 200 OK\r\n".encode())
            conn.send("Content-Type: text/css\r\n".encode())
            conn.send("\r\n".encode())
            f1 = open("main_en.css", "rb")
            conn.send(f1.read())
        #png image
        elif path == "/.png":
            conn.send("HTTP/1.1 200 OK\r\n".encode())
            conn.send("Content-Type: image/png\r\n".encode())
            conn.send("\r\n".encode())
            f1 = open("bzu.png", "rb")
            conn.send(f1.read())
        #jpg image
        elif path == "/.jpg":
            conn.send("HTTP/1.1 200 OK\r\n".encode())
            conn.send("Content-Type: image/jpg\r\n".encode())
            conn.send("\r\n".encode())
            f1 = open("wallpaper.jpg", "rb")
            conn.send(f1.read())
        #To get the style of English page
        elif path == "/main_en.css":
            conn.send("HTTP/1.1 200 OK\r\n".encode())
            conn.send("Content-Type: text/css\r\n".encode())
            conn.send("\r\n".encode())
            f1 = open("main_en.css", "rb")
            conn.send(f1.read())
            f1.close()

        #To get the logo of English & Arabic page
        elif path == "/bzu.png":
            conn.send("HTTP/1.1 200 OK\r\n".encode())
            conn.send("Content-Type: image/png\r\n".encode())
            conn.send("\r\n".encode())
            f1 = open("bzu.png", "rb")
            conn.send(f1.read())
            f1.close()
        elif path == "/main_ar.css":
            conn.send("HTTP/1.1 200 OK\r\n".encode())
            conn.send("Content-Type: text/css\r\n".encode())
            conn.send("\r\n".encode())
            f1 = open("main_ar.css", "rb")
            conn.send(f1.read())
            f1.close()

        elif path == "/cr":
            conn.send("HTTP/1.1 307 Temporary Redirect\r\n".encode())
            conn.send("Location: https://cornell.edu/\r\n".encode())
            conn.send("\r\n".encode())
        elif path == "/so":
            conn.send("HTTP/1.1 307 Temporary Redirect\r\n".encode())
            conn.send("Location: https://stackoverflow.com/\r\n".encode())
            conn.send("\r\n".encode())
        elif path == "/rt":
            conn.send("HTTP/1.1 307 Temporary Redirect\r\n".encode())
            conn.send("Location: https://ritaj.birzeit.edu/\r\n".encode())
            conn.send("\r\n".encode())
        else:
            conn.send("HTTP/1.1 404 Not Found\r\n".encode())
            conn.send("Content-Type: text/html\r\n".encode())
            conn.send("\r\n".encode())
            error= open("error.html","rb")
            conn.send(error.read())
            conn.send(f'IP: ({ip})  Port: ({port})'.encode())
            error.close()

    conn.close()