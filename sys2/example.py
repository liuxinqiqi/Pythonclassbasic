import threading
from time import sleep

data = 0

def a(e):
    e.wait()
    global data
    data = 10
    sleep(0.5)
    print "process a :",data

def b(e):
    global data
    data = 100
    print "process b:",data
    e.set()

if __name__ == '__main__':
    e = threading.Event()
    w1 = threading.Thread(target = a,args = (e,))

    w1.start()

    w2 = threading.Thread(target = b,args = (e,))

    w2.start()

    print 'main : waiting before calling Event.set()'
    sleep(2)
    print 'over'
