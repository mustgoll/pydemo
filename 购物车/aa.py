class a:
	"""docstring for a"""
	def __init__(self, arg):
		self.arg = arg
		
	def b(self,name):
		print (self.arg,name)

qq=input('>>:').strip()
getattr(a(1),qq)(2)