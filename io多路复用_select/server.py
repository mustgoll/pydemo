import socket,select

s=socket.socket()
s.bind(('127.0.0.1',8888))
s.listen(5)
s.setblocking(False)
inputs=[s,]
outputs=[]


while True:
    r, w, e = select.select(inputs, outputs, inputs)
    print(1)
    for i in r:
        if i is s:
            conn,addr=i.accept()
            print('收到一个新链接：',addr)
            inputs.append(conn)
        else:
            data=i.recv(1024)
            print('收到：%s' % data)
            i.sendall(data.upper())