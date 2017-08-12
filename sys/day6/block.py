#!/usr/bin/python
#coding=utf-8

from socket import *

def start():
    try:
        sock = socket(AF_INET,SOCK_STREAM)
        sock.bind(('127.0.0.1',8888))
        sock.listen(5)
    except Exception as e:
        print "fail"
        exit(0)
    while True:
        sock.setblocking(False)
        clientsock,clientaddr = sock.accept()
        
        buf = clientsock.recv(1024)
        clientsock.send(buf)
        clientsock.close()
        print "+++++++++"

if __name__ == "__main__":
    start()
