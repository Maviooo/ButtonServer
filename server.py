#!/usr/bin/python3
import socket
import sys
import threading

def on_new_client(clientsocket,addr):
    while True:
        msg = clientsocket.recv(1024)
        #do some checks and if msg == someWeirdSignal: break:
        print (addr, " >> ", msg)
        #Maybe some code to compute the last digit of PI, play game or anything else can go here and when you are done.
        clientsocket.send(msg)
    clientsocket.close()

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 6960)
print(sys.stderr, 'starting up on %s port %s' % server_address)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)
while True:
   c, addr = sock.accept()     # Establish connection with client.
   threading._start_new_thread(on_new_client,(c,addr))
sock.close()