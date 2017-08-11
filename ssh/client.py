import socket
client=socket.socket()
client.connect(('localhost',8000))
while True:
	cmd=input('请输入cmd命令：')
	client.send(cmd.encode('utf-8'))
	data_len=client.recv(1024).decode('utf-8')
	print('len:',data_len)
	while True:
		data=client.recv(1024).decode('utf-8')
		print(data)
		if len(data.encode('utf-8'))<1024:
			break
client.close()