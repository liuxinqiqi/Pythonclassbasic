#!/usr/bin/python

from socket import *
import sys
import os

class Node(object):
    def __init__(self,val,next = None):
        self.val = val
        self.next = next

def do_login(s,H,msg,clientaddr):
    msg = msg.split(' ')
    msg[2] = '%s login....'%msg[1]
    
    p  = Node(clientaddr)
    q = H.next

    while q != None:
        s.sendto(msg[2],q.val)
        q = q.next

    p.next = H.next
    H.next = p
    
    return

def do_quit(s,H,msg,clientaddr):
    msg = "%s log out..."%msg.split(' ')[1]

    p = H

    while p.next != None:
        if p.next.val != clientaddr:
            s.sendto(msg,p.next.val)
            p = p.next

        else:
            q = p.next
            p.next = q.next

    return
    

def do_chat(s,H,msg,clientaddr):
    p = H.next
    buf = "%s say %s"%(msg.split(' ')[1],msg.split(' ')[2])

    while p != None:
        if p.val != clientaddr:
            s.sendto(buf,p.val)
        p = p.next

    return

def do_parent(s,addr):
    #msg = type + name + text
    msg = "B server "

    while True:
        print "system message >>"
        text = sys.stdin.readline()
        msg = msg + text
        s.sendto(msg,addr)
    s.close()

def do_child(s):
    H = Node(None)

    while True:
        msg,clientaddr = s.recvfrom(4096)
        tmp = msg.split(' ')

        if tmp[0] == 'L':
            do_login(s,H,msg,clientaddr)
        if tmp[0] == 'B':
            do_chat(s,H,msg,clientaddr)
        if tmp[0] == 'Q':
            do_quit(s,H,msg,clientaddr)

    return

def main():
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)

    s = socket(AF_INET,SOCK_DGRAM,0)
    s.bind(ADDR)

    pid = os.fork()

    if pid < 0:
        print "fail to create process"
        return
    elif pid == 0:
        do_child(s)
    else:
        do_parent(s,ADDR)


if __name__ == "__main__":
    main()
