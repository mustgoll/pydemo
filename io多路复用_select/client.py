import socket

c=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(('127.0.0.1',8888))
while True:
    msg=input('>>')
    c.sendall(msg.encode())
    data=c.recv(1024)
    print(data.decode())