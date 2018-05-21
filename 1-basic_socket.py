#!/usr/bin/env python3
import socket

IP = '0.0.0.0'
PORT = 1234
MAXIMUM_QUEUE_SIZE = 0

listening_socket = socket.socket()
listening_socket.bind((IP, PORT))

listening_socket.listen(MAXIMUM_QUEUE_SIZE)
print("Hello, I'm waiting for a connection")

(client_socket, client_ip_and_port) = listening_socket.accept()
response = "Hi there, here's my response :), bye\n".encode()
client_socket.send(response)

print("Well, I've had enough, I'll quit now")
client_socket.close()
