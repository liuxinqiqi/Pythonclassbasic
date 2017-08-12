#!/usr/bin/python
#coding=utf-8

import socket
import struct
import sys
from time import sleep

message = "very important data"
message1 = "very very important data"

multicast_group = ('224.3.29.71',10000)
multicast_group1 = ('224.3.29.72',10001)

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sock.settimeout(3)

ttl = struct.pack('b',1) #将数字1 转换成无符号字符类型。在python中没有这种类型但是内核需要所以需要这样转变

sock.setsockopt(socket.IPPROTO_IP,socket.IP_MULTICAST_TTL,ttl)

try:
    while True:

        sleep(2)
        sent = sock.sendto(message,multicast_group)
        sent = sock.sendto(message1,multicast_group1)

        print >>sys.stderr,'waiting to receive'
        try:
            data,server = sock.recvfrom(16)
        except socket.timeout:
            print sys.stderr,'timed out,no more responses'
            break
        else:
            print >>sys.stderr,'received "%s" from %s'%(data,server)
finally:
    print >>sys.stderr,'closing socket'
    sock.close()

