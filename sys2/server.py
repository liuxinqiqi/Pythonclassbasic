#!/usr/bin/python

from socket import *
from time import ctime
import sys

HOST = '192.168.0.3'
PORT = int(sys.argv[1])
BUFSIZE = 1024
ADDR = (HOST,PORT)

sockfd = socket(AF_INET,SOCK_STREAM)

sockfd.bind(ADDR)

sockfd.listen(5)

while True:
    print "waiting for connection....."

    connfd,addr = sockfd.accept()

    print "connected from :",addr

    while True:
        data = connfd.recv(BUFSIZE)
        if  not data:
            break
        connfd.send("[%s] : %s"%(ctime(),data))


sockfd.close()
connfd.close()
