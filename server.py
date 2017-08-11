import socket
server = socket.socket()
server.bind(('localhost',8000))
server.listen(3)
conn,addr=server.accept()
q=True
while q:
	data = conn.recv(300).decode('utf-8')
	print('客户端：',data)
	if data=='q':
		break
	# a=input('这里是服务端：')
	with open('ceshi.avi','rb') as f:
		a=f.read()
		conn.sendall(a)
server.close()

