#!/usr/bin/python

from socket import *
import sys

HOST = sys.argv[1]
PORT = int(sys.argv[2])
BUFSIZE = 1024
ADDR = (HOST,PORT)

sockfd = socket(AF_INET,SOCK_STREAM)

sockfd.connect(ADDR)
while True:
    data = raw_input('>')

    if not data:
        break

    sockfd.send(data)
    data = sockfd.recv(BUFSIZE)

    
    print data

sockfd.close()
