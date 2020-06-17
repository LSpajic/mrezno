import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.0.107',8080))
s.send(b"Hello world\n")
while 1:
    unos = input()
    if unos.lower()=="kraj":
        break
    s.send((unos + "\n").encode())