#!/usr/bin/python

from socket import *
import sys
from signal import *
import os


def do_child(s,addr,msg):
    name = msg.split(' ')[1]
    while True:
        text = raw_input(">>")

        if text == 'quit':
            msg = 'Q ' + name
            s.sendto(msg,addr)
            os.kill(os.getppid(),SIGKILL)
            exit()
        else:
            msg = 'B %s %s'%(name,text)
            s.sendto(msg,addr)
    return

def do_parent(s):
    while True:
        msg,addr = s.recvfrom(2048)
        print msg

def main():
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)
    
    s = socket(AF_INET,SOCK_DGRAM,0)

    name = raw_input("please input your name>>")

    msg = 'L %s '%name

    s.sendto(msg,ADDR)

    pid = os.fork()

    if pid < 0:
        print "fail to create process"
        return
    elif pid == 0:
        do_child(s,ADDR,msg)
    else:
        do_parent(s)
        

if __name__ == "__main__":
    main()
