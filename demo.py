import time
def aa(fun):
	def c(*arg,**arg1):
		start=time.time()
		fun(*arg,**arg1)
		end=time.time()
		print ('this time is %s' %(end-start))
	return c
@aa
def a():
	time.sleep(3)
	print ('this is a')
# a=aa(a)
a()
@aa
def b(name):
	time.sleep(3)
	print ('b is',name)
b('helin')