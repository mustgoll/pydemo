import socket
import os
client=socket.socket()
client.connect(('localhost',8000))
q=True
while q:
	a=input('这里是客户端：')
	client.send(a.encode('utf-8'))
	if a=='q':
		break
	while True:
		data=client.recv(20000)
		with open('ceshi2.avi','ab') as f:
			f.write(data)
		if len(data)<20000:
			break
	# print('服务端：',data)

client.close()