import socket
client=socket.socket()
client.connect(('localhost',8000))
while True:
	msg=input('>>:')
	if len(msg)==0:continue
	client.send(msg.encode())
	if msg=='q':
		break
	data=client.recv(1024)
	print(data.decode())
client.close()