import socket
import sys
from time import sleep

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

clientSocket.connect(("127.0.0.1", int(sys.argv[1])));

data = "Hello Server!";

clientSocket.send(data.encode());

dataFromServer = clientSocket.recv(1024);
print(dataFromServer.decode());
while True:
    input("Press Enter to continue...")
    clientSocket.send("Button pressed!!!".encode());
clientSocket.close()
