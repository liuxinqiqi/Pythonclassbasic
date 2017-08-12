#!/usr/bin/python

from signal import *


alarm(3)

signal(SIGALRM,SIG_DFL)
signal(SIGALRM,SIG_IGN)

while True:
    pass
