#!/usr/bin/env python3
import socket

IP = '127.0.0.1'
PORT = 1234
MAXIMUM_QUEUE_SIZE = 0
BUFFER_SIZE = 2048

server_socket = socket.socket()
server_socket.bind((IP, PORT))

server_socket.listen(MAXIMUM_QUEUE_SIZE)
print("Hello, I'm waiting for incoming connections")

while True:
    (client_socket, client_ip_and_port) = server_socket.accept()
    initial_response = "hi there, I can echo whatever you tell me\n".encode()
    client_socket.send(initial_response)

    client_message = client_socket.recv(BUFFER_SIZE).decode()
    echo_response = ("You said: %s" % client_message).encode()
    client_socket.send(echo_response)

    final_response = ("Thanks for using my server, see you later.\n").encode()
    client_socket.send(final_response)

    client_socket.close()
