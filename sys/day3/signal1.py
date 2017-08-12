#!/usr/bin/python

from signal import *
import os,time

def recvive_sig(signum,stack):
    if signum == SIGINT:
        print "keep......"
    elif signum == SIGALRM:
        print "receive a alarm"
    else:
        print "other signal"



alarm(7)

signal(SIGINT,recvive_sig)
signal(SIGALRM,recvive_sig)

print "My PID is :",os.getpid()

while True:
    print "Waiting...."
    time.sleep(2)
