import socket,hashlib
client=socket.socket()
client.connect(('localhost',8000))
while True:
	cmd=input('what help：')
	if len(cmd)==0:
		continue
	client.send(cmd.encode())
	file_size=client.recv(1024).decode()
	if file_size=='1':
		print('该文件不存在')
		continue
	print('原文件大小：',file_size)
	client.send(b'lt is go...')
	filename=cmd.split()[1]
	m=hashlib.md5()
	with open(filename+'.bak','wb') as f:
		get_size=0
		while get_size<int(file_size):
			data=client.recv(1024)
			m.update(data)
			f.write(data)
			get_size+=len(data)
		md=m.hexdigest()
	client.send(md.encode()) #传输完成代码
	print(client.recv(1024))
	print('MD5:',md)
client.close()