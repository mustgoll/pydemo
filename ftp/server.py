import socket
import os,hashlib
server=socket.socket()
server.bind(('localhost',8000))
server.listen()
while True:
	conn,addr=server.accept()
	print('客户端',addr,'已连接')
	while True:
		data = conn.recv(1024).decode('utf-8')
		if not data:
			break
		action,filename=data.split()
		if os.path.isfile(filename):
			print(action,'(',filename,')')
			file_size=os.stat(filename).st_size
			conn.send(str(file_size).encode())
			conn.recv(1024)
			print('开始传输...')
			m=hashlib.md5()
			with open(filename,'rb') as f:
				f=f.read()
				m.update(f)
				conn.sendall(f)
			mb=m.hexdigest()
			print('MD5:',mb)
			md=conn.recv(1024).decode() #收到表示传输完成
			if md==mb:
				print(filename,'传输完成')
				conn.send(b'OK Success!')
			else:
				print(filename,'传输失败')	
		else:
			print('文件不存在！')
			conn.send(b'1')
	print('客户端',addr,'已断开')
print('服务端关闭')
server.close()