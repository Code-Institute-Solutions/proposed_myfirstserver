import datetime
import socket

IP = '0.0.0.0'
PORT = 8080
MAXIMUM_QUEUE_SIZE = 0
BUFFER_SIZE = 2048


def show_time():
    now = datetime.datetime.now()
    response_headers = "HTTP/1.1 200 OK\n\n"
    response_body = "The time is %s" % now.strftime("%H:%M:%S")
    return (response_headers + response_body).encode()


def read_file(resource_as_path):
    # This is actually very unsafe. To secure this, we must first
    # sanitize the path to prevent a directory traversal attack
    relative_path = resource_as_path[1:]

    try:
        response_headers = 'HTTP/1.1 200 OK\n\n'
        with open(relative_path) as f:
            response_body =  f.read()
    except IOError:
        response_headers = 'HTTP/1.1 404 Not Found\n\n'
        response_body = "Could not read the requested file"
    return (response_headers + response_body).encode()

def echo_request(request):
    response_headers = "HTTP/1.1 200 OK\n\n"
    response_body = "Your request was:\n" + request
    return (response_headers + response_body).encode()


def respond(client_socket, client_ip_and_port):
    request = client_socket.recv(BUFFER_SIZE).decode()
    request_line = request.splitlines()[0]
    (method, resource, version) = request_line.split()

    if resource == "/time":
        response = show_time()
    elif resource == "/echo":
        response = echo_request(request)
    else:
        response = read_file(resource)

    client_socket.send(response)


def serverloop():
    listening_socket = socket.socket()
    listening_socket.bind((IP, PORT))
    listening_socket.listen(MAXIMUM_QUEUE_SIZE)

    while True:
        (client_socket, client_ip_and_port) = listening_socket.accept()
        respond(client_socket, client_ip_and_port)
        client_socket.close()


if __name__ == '__main__':
    print('Server launched on %s:%s, press ctrl+c to kill the server'
          % (IP, PORT))
    serverloop()
