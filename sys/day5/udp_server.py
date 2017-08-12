#!/usr/bin/python

from socket import *
from time import ctime

HOST = '192.168.1.3'
PORT = 8888
BUFSIZE = 1024
ADDR = (HOST,PORT)

sockfd = socket(AF_INET,SOCK_DGRAM)

sockfd.bind(ADDR)

while True:
    print "waiting for message"

    data,addr = sockfd.recvfrom(BUFSIZE)

    print "client addr :",addr

    sockfd.sendto('[%s] : %s'%(ctime(),data),addr)


sockfd.close()
