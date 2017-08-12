#!/usr/bin/python


from socket import *
import sys

HOST = sys.argv[1]
PORT = int(sys.argv[2])

BUFSIZE = 1024
ADDR = (HOST,PORT)

sockfd = socket(AF_INET,SOCK_DGRAM)

while True:
    data = raw_input('>')
    if not data:
        break

    sockfd.sendto(data,ADDR)

    data,ADDR = sockfd.recvfrom(BUFSIZE)
    print data

#print sockfd.fileno()
sockfd.close()

