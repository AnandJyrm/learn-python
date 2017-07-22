#! /usr/bin/python
# server using python sockets
import socket
import sys
import thread

HOST = ""  # symbolic name meaning all available interfaces
PORT = 8888  # arbitrary non-privileged port

# create socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except:
    print "Socket creation error"
    sys.exit()

# bind socket
try:
    s.bind((HOST, PORT))
except:
    print "Socket bind error"
    sys.exit()

# listen on socket
s.listen(10)


def handleClient(conn):
    conn.send("Welcome to server\n")
    # keep the connection thread running till client disconnects
    while True:
        # receive from client
        data = conn.recv(1024)
        reply = "OK... " + data
        if not data:
            break
        conn.sendall(reply)

    # close connection when loop ends
    conn.close()


# to handle multiple clients
while 1:
    # wait to accept a connection
    conn, addr = s.accept()
    print "connected with " + addr[0] + " : " + str(addr[1])

    thread.start_new_thread(handleClient, (conn,))

s.close()
