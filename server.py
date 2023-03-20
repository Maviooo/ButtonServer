#!/usr/bin/python3

import socket
import sys
import threading
from time import sleep

clients_ids = []

def on_new_client(clientsocket, addr):
    msg = clientsocket.recv(1024)
    print (addr, " >> ", msg.decode())
    clients_ids.append(addr)
    clientsocket.send(f"You are user {clients_ids.index(addr)}".encode())
    while True:
        print(wait_on_press(clientsocket, addr))
        send_id_to_all()
        print("Ready for new button press")
    clientsocket.close()

def wait_on_press(clientsocket, addr):
    while(clientsocket.recv(1024)):
        sock.setblocking(1)
        return (f"Button pressed id {clients_ids.index(addr)}")
    

def send_id_to_all():
    sleep(5)
    sock.setblocking(0)
    return

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', int(sys.argv[1]))
print('Starting up on %s port %s' % server_address)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)
while True:
   c, addr = sock.accept()     # Establish connection with client.
   threading._start_new_thread(on_new_client,(c,addr))
sock.close()