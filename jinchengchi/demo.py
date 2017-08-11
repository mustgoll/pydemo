from multiprocessing import Pool
import time,os
def run():
    time.sleep(1)
    print(os.getpid())
    return os.getpid()
def cb(m):
    print('回调：',m,os.getpid())
if __name__=='__main__':
    print('far:',os.getpid())
    pool=Pool(3)
    for i in range(10):
        pool.apply_async(func=run,callback=cb)
    pool.close()
    pool.join()
