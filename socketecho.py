#!/usr/bin/env python3
import socket

IP = '127.0.0.1'
PORT = 1234
MAXIMUM_QUEUE_SIZE = 0
BUFFER_SIZE = 2048

listening_socket = socket.socket()
listening_socket.bind((IP, PORT))

listening_socket.listen(MAXIMUM_QUEUE_SIZE)
print("Hello, I'm waiting for a connection")


(clientsocket, client_ip_and_port) = listening_socket.accept()
while True:
    client_message = clientsocket.recv(BUFFER_SIZE).decode()
    response = ("You said: %s" % client_message).encode()
    clientsocket.send(response)
