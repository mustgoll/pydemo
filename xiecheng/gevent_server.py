import gevent,socket
from gevent import monkey
monkey.patch_all()
def server(port):
    s=socket.socket()
    s.bind(('127.0.0.1',port))
    s.listen(200)
    while True:
        con,addr=s.accept()
        print(addr,con)
        gevent.spawn(handle,con)
        # handle(con)

def handle(con):
    while True:
        data=con.recv(1024)
        print(data.decode())
        con.send(data.upper())


server(8888)