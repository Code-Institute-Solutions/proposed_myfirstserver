#!/usr/bin/env python3
import os
import socket


IP = '127.0.0.1'
PORT = 1234
MAXIMUM_QUEUE_SIZE = 0
BUFFER_SIZE = 2048


def read_file(url_as_path):
    # This is actually very unsafe. To secure this, we must first
    # sanitize the path to prevent a directory traversal attack
    relative_path = url_as_path[1:]
    with open(relative_path) as f:
        return f.read()


def respond(client_socket, client_ip_and_port):
    request = client_socket.recv(BUFFER_SIZE).decode()
    request_line = request.splitlines()[0]
    (method, resource, http_version) = request_line.split()

    try:
        response_headers = 'HTTP/1.1 200 OK\n\n'
        response_body = read_file(resource)
    except IOError:
        response_headers = 'HTTP/1.1 404 OK\n\n'
        response_body = "Could not read the requested file"

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