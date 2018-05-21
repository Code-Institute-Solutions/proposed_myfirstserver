#!/usr/bin/env python3
import socket

IP = '0.0.0.0'
PORT = 8080
MAXIMUM_QUEUE_SIZE = 0
BUFFER_SIZE = 2048


def respond(client_socket, client_ip_and_port):
    request = client_socket.recv(BUFFER_SIZE).decode()
    response_headers = 'HTTP/1.1 200 OK\n\n'
    response_body = ("Your request was:\n" + request)
    encoded_response = (response_headers + response_body).encode()
    client_socket.send(encoded_response)


def server_loop():
    server_socket = socket.socket()
    server_socket.bind((IP, PORT))
    server_socket.listen(MAXIMUM_QUEUE_SIZE)

    while True:
        (client_socket, client_ip_and_port) = server_socket.accept()
        respond(client_socket, client_ip_and_port)
        client_socket.close()


if __name__ == '__main__':
    print('Server launched on %s:%s. Press ctrl+c to kill the server'
          % (IP, PORT))
    server_loop()