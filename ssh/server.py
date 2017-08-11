import socket
import os
server=socket.socket()
server.bind(('localhost',8000))
server.listen()
conn,addr=server.accept()
while True:
	data = conn.recv(1024).decode('utf-8')
	if not data:
		print('客户端已断开')
		break
	print('this is connect: ',addr,data)
	cmd_res=os.popen(data).read()
	if not cmd_res:
		cmd_res='is Error CMD'
	conn.send(str(len(cmd_res)).encode('utf-8'))
	conn.sendall(cmd_res.encode('utf-8'))
server.close()