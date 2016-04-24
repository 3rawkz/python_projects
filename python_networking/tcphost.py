# A basic iterative server script in Python 3.5 that returns client strings
# in UPPERCASE
import socket


def main():
    host = '127.0.0.1'  # the local IP of the server (this one is for vir testing)
    port = 5000  # the port in which the client must send requests and connect

    receiving_socket = socket.socket()
    receiving_socket.bind((port, host))  # linking machines IP,port,and socket

    receiving_socket.listen(1)  # connections at a time - if n_con > 1: use queue
    cur_connection, sender_address = receiving_socket.accept()
    print('Connection from:' + str(sender_address))
    while True:
        data = cur_connection.recv(1024)  # buffer size
        if not data:
            break
        print('From connected user: ' + str(data))
        data = str(data).upper()
        print('Returned to client: ' + str(data))
        cur_connection.send(bytes(data, 'utf-8'))
    cur_connection.close()
if __name__ == '__main__':
    main()
