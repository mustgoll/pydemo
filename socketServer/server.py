import socketserver
class MyTcp(socketserver.BaseRequestHandler):
	"""docstring for MyTcp"""
	def handle(self):
		while True:
			try:
				self.data=self.request.recv(1024).strip()
				if self.data==b'q' or not self.data:
					break
				print(self.client_address[0],':',self.client_address[1],self.data)
				self.request.send(self.data.upper())
			except ConnectionResetError as e:
				print('Error:',e)
				break
		print(self.client_address[0],':',self.client_address[1],'连接已断开')
if __name__ == '__main__':
	HOST,PORT='localhost',8000
	server=socketserver.ThreadingTCPServer((HOST,PORT),MyTcp)
	server.serve_forever()
