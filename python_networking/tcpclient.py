import socket


def main():
    host = '192.168.0.1'
    port = 5000

    requesting_socket = socket.socket()
    requesting_socket.connect((host, port))

    message = input("->")
    while message != 'q':
        requesting_socket.send(message)
        data = requesting_socket.recv(1024)
        print('Received from server: ' + str(data))
        message = input("->")
    requesting_socket.close()

if __name__ == '__main__':
    main()
