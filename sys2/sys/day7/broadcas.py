#!/usr/bin/python

import socket,sys
from time import sleep

dest = ('<broadcast>',9999)

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
print "Looking for replise;press Ctrl -C to stop"

while True:
    sleep(1)
    s.sendto("Hello",dest)
    (buf,address) = s.recvfrom(2048)
    if not len(buf):
        break
    print "Received from %s:%s"%(address,buf)
