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


(client_socket, client_ip_and_port) = listening_socket.accept()
initial_response = "hi there, I can echo whatever you tell me\n".encode()
client_socket.send(initial_response)

client_message = client_socket.recv(BUFFER_SIZE).decode()
echo_response = ("You said: %s" % client_message).encode()
client_socket.send(echo_response)

print("Well, I've had enough, I'll quit now")
client_socket.close()
