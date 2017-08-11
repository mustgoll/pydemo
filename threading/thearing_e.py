import threading
import time
m=0
def run(n):
    global m
    print('q:',n)
    time.sleep(2)
    m=m+1
q1=threading.Thread(target=run,args=('1',))
q2=threading.Thread(target=run,args=('2',))
q3=threading.Thread(target=run,args=('3',))
q4=threading.Thread(target=run,args=('4',))
q5=threading.Thread(target=run,args=('5',))
q6=threading.Thread(target=run,args=('6',))
q1.start()
q2.start()
q3.start()
q4.start()
q5.start()
q6.start()
time.sleep(2.5)
print(m)