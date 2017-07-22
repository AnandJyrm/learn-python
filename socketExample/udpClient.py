#! /usr/bin/python
# udp client

import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except:
    print "Socket create failed"
    sys.exit()

HOST = "localhost"
PORT = 8888

while(1):
    msg = raw_input("Enter message to send: ")

    try:
        s.sendto(msg, (HOST, PORT))

        d = s.recvfrom(1024)
        reply = d[0]
        addr = d[1]

        print "Server reply : " + reply
    except:
        print "Send and Receive failed"
        sys.exit()
