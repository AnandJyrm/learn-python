#! /usr/bin/python
# python socket example -- server
import socket
import sys
from time import sleep

HOST = ""  # symbolic name meaning all available interfaces
PORT = 8888  # arbitrary non-privileged port

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Socket created"
except:
    print "Socket creation failed"
    sys.exit()

try:
    s.bind((HOST, PORT))
    print "socket bind complete"
except:
    print "socket bind error"
    sys.exit()

s.listen(10)
print "Socket now listening"
while 1:
    # wait to accept a connection blocking
    conn, addr = s.accept()

    # display client information
    print "connected with " + addr[0] + " : " + str(addr[1])
    data = conn.recv(1024)
    if not data:
        break
    reply =" OK..." + data
    conn.sendall(reply)
conn.close()
s.close()
