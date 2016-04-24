import socket


def main():
    host = '192.168.0.8'  # the IP of the server
    port = 5000  # the port in which the client must connect

    receiving_socket = socket.socket()
    receiving_socket.bind((host, port))

    receiving_socket.listen(1)  # connections at a time - use queue > 1
    cur_connection, sender_address = receiving_socket.accept()
    print('Connection from:' + str(sender_address))
    while True:
        data = cur_connection.recv(1024)  # buffer size in bits
        if not data:
            break
        print('From connected user: ' + str(data))
        data = str(data).upper()
        print('...sending: ' + str(data))
        cur_connection.send(bytes(data, 'utf-8'))
    cur_connection.close()
if __name__ == '__main__':
    main()
