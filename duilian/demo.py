import threading,time,queue
qo=queue.Queue()
def out(m):
    for i in range(10):
        qo.put('%s%s' %(m,i))
        print('out:%s%s' %(m,i))
        time.sleep(1)
q=threading.Thread(target=out,args=('hl',))
q.start()
def in1():
    for i in range(10):
        print('in:',qo.get(timeout=1.2))
qi=threading.Thread(target=in1,)
qi.start()