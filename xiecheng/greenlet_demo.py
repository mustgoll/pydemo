import greenlet

def a():
    print(1)
    bb.switch()
    print(2)
    bb.switch()

def b():
    print(3)
    aa.switch()
    print(4)

aa=greenlet.greenlet(a)
bb=greenlet.greenlet(b)
aa.switch()