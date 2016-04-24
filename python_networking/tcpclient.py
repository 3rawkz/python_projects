import socket


def main():
    host = '127.0.0.1'  # pointer address for host if on same machine as client
    port = 5000  # the port on the host machine to which our request will be sent

    requesting_socket = socket.socket()
    requesting_socket.connect((host, port))

    message = input("->")
    while message != 'q':
        requesting_socket.send(bytes(message, 'utf-8'))  # specifies char encoding
        data = requesting_socket.recv(1024)  # size of the buffer
        print('Received from server: ' + str(data))
        message = input("->")
    requesting_socket.close()

if __name__ == '__main__':
    main()
