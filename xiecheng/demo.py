import time
def a(name):
    while True:
        c=yield
        print('get name:',c)
def b():
    a1.__next__()
    x=0
    while x<10:
        a1.send(x)
        time.sleep(1)
        print('make name')
        x+=1

if __name__=='__main__':
    a1=a('helin')
    b()