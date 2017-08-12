from time import ctime,sleep
import threading

class MyThread(threading.Thread):
    def __init__(self,func,args,name = ''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def run(self):
        self.func(*self.args)

def super_player(file,time):
    for i in range(2):
        print('Start playing: %s .%s'%(file,ctime()))
        sleep(time)

l = {'Baby.mp3':3,'Avatar.mp4':5,'You and me.mp3':4}

threads =[]
files = range(len(l))

for file,time in l.items():
    t = MyThread(super_player,(file,time))
    threads.append(t)

if __name__ == '__main__':
    for i in files:
        threads[i].start()

    for i in files:
        threads[i].join()

    print "+++++++++++++++++++++++++++++++++++++++++++"
