#!/usr/bin/env python3
import socket

IP = '127.0.0.1'
PORT = 1234
MAXIMUM_QUEUE_SIZE = 0

serversocket = socket.socket()
serversocket.bind((IP, PORT))

serversocket.listen(MAXIMUM_QUEUE_SIZE)
print("Hello, I'm waiting for connections")

(clientsocket, client_ip_and_port) = serversocket.accept()
clientsocket.send(b"Hi user, here's my response :)\n")

print("Well, I've had enough, I'll quit now")
