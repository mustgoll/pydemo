import socket

def client():
    cl=socket.socket()
    cl.connect(('127.0.0.1',8888))
    while True:
        msg=input('>>')
        cl.send(msg.encode('utf-8'))
        data=cl.recv(1024)
        print(data.decode())
    cl.close()
client()