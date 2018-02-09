#!/usr/bin/env python3
"""A very very basic http server"""
# The socket library which lets us create network connections:
import socket

# The ip address to listen on:
# 127.0.0.1 (aka localhost) only listens to requests from the local computer
# set to 0.0.0.0 in order to accept requests from entire network
IP = '127.0.0.1'
# Port number to listen on:
# use any number from 1024 to 65535 (lower numbers are reserved)
PORT = 1234
# Number of connections to allow to queue up before rejecting new ones
MAXIMUM_QUEUE_SIZE = 5
# The amount of bytes we read from the socket at a time:
# basic requests are shorter than this, but to handle longer requests we'd
# need to receive multiple times
BUFFER_SIZE = 2048


def respond(socket, client_ip_and_port):
    """Handle a single request from a client socket

    HTTP requests arrive as a sequence of bytes that contain one or more lines
    of headers containing the request details, terminating with an empty line.
    (Some request types (e.g. POST) also contain a data section after
    the empty line)

    The response we're constructing has a similar structure, one or more
    response headers, then an empty line and then the response body, which
    is usually HTML (other common choices are JSON or XML).

    A server generally crafts a response based on the specific request
    details. In this example, we just return a list with the request headers.
    """
    # Receive the request from the socket:
    # It arrives as a sequence of bytes, so we first decode it to text
    request = socket.recv(BUFFER_SIZE).decode()
    # Split the request into separate lines (each a header) and discard last
    # empty line
    request_headers = request.splitlines()[:-1]

    # The header section we'll return, ending with an empty line:
    response_headers = 'HTTP/1.1 200 OK\n\n'
    # Our html response heading:
    response_body_heading = ('<h1>Hi there at %s:%s, ' % client_ip_and_port +
                             'here are your request headers:</h1>')
    # Some more html to display the request headers as an unordered list:
    response_body_ul = ('<ul><li>%s</li></ul>' %
                        '</li><li>'.join(request_headers))
    # Collect the response parts and encode as a byte sequence:
    encoded_response = (response_headers +
                        response_body_heading + response_body_ul).encode()
    # Send the response across the socket:
    socket.send(encoded_response)


def serverloop():
    """Open a server socket connection and accept incoming client connections

    A connection consists of a pair of sockets, one for the server and one for
    the client, each defined by an IP address which identifies the computer,
    and a port number that identifies the process.
    So a computer can have multiple sockets open at the same time, but each
    has to use a separate port.
    We create a server socket to listen on a preselected port, and we accept
    incoming client connections, which generally use any available port.
    For each connection established we get the client socket and
    handle it in our `respond` function.
    """
    # Create a regular internet socket (TCP/IP):
    serversocket = socket.socket()
    # Bind the socket to listen on a specific port on our computer:
    serversocket.bind((IP, PORT))
    # Begin listening on the socket, with a particular queue size:
    serversocket.listen(MAXIMUM_QUEUE_SIZE)

    # Do this forever (until server process is killed):
    while True:
        # Accept a connection from next client:
        # for each connection we get the socket and connection details
        (clientsocket, client_ip_and_port) = serversocket.accept()
        # Process the client's request:
        respond(clientsocket, client_ip_and_port)
        # Close the client connection:
        clientsocket.close()


if __name__ == '__main__':
    print('Server launched on %s:%s press ctrl+c to kill the server'
          % (IP, PORT))
    serverloop()
