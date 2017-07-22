#! /usr/bin/python
# Socket client example in python
import socket  # for sockets
import sys  # for exit
from time import sleep

# create an AF_INET, STREAM socket (tcp)
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Socket Created"
    print s
except socket.error, msg:
    print "Error" + str(msg[0])
    sys.exit()

host = "localhost"
port = 8888

try:
    remote_ip = socket.gethostbyname(host)
    print "Ip address of " + host + " is " + remote_ip
except socket.gaierror:
    print "host could not be resolved"
    sys.exit()

s.connect((remote_ip, port))
print "Socket Connected to " + host + " on port %d" % port

# Send some data to remote server
message = "mew"
while 1:
    try:
        # set the whole string
        s.sendall(message)
    except socket.error:
        print "Send Failed"
        sys.exit()

    sleep(10)
    # To receive data
    try:
        reply = s.recv(4096)
        print reply
    except:
        print "something happened with recv"
        sys.exit()
    message = reply

s.close()
