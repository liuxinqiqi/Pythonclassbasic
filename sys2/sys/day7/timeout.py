#!/usr/bin/python

import traceback
from socket import *

HOST = ""
PORT = 9999

s = socket()

s.settimeout(3)

s.bind((HOST,PORT))

s.listen(1)

while True:
    try:
        conn,addr = s.accept()
        print "s time out ......."
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        continue
    conn.settimeout(3)
    
    try:
        print "GOt connection from:",conn.getpeername()

        while True:
            data = conn.recv(1024)

            if not len(data):
                break
            conn.sendall(data)
    except (KeyboardInterrupt,SystemExit):
        raise
    except timeout:
        print "time out ...."
    except:
        traceback.print_exc()

    conn.close()


