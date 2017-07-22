#! /usr/bin/python
# simple udp server

import socket
import sys

HOST = ''
PORT = 8888
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except:
    print "Socket create error"
    sys.exit()
try:
    s.bind((HOST, PORT))
except:
    print "Socket bind error"
    sys.exit()

while 1:
    d = s.recvfrom(1024)
    data = d[0]
    addr = d[1]

    if not data:
        break

    reply = "OK... " + data

    s.sendto(reply, addr)
    print "Message[" + addr[0] + ":" + str(addr[1]) + "] - " + data.strip()

s.close()
