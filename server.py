# -*- coding: utf-8 -*-
import socket
import select


def main():
    server_socket = socket.socket()
    server_socket.bind(('0.0.0.0', 23))
    server_socket.listen(5)
    open_client_sockets = []
    massages_to_send = []

    def send_waiting_massages(wlist):
        for massage in massages_to_send:
            (client_socket, data) = massage
            if client_socket in wlist:
                client_socket.send(data)
                massages_to_send.remove(massage)

    while True:
        rlist, wlist, xlist = select.select([server_socket] + open_client_sockets, open_client_sockets, [])
        for current_socket in rlist:
            if current_socket is server_socket:
                (new_socket, address) = server_socket.accept()
                open_client_sockets.append(new_socket)
            else:
                data = current_socket.recv(1024)
                if data == "":
                    open_client_sockets.remove(current_socket)
                    print "connection with client closed"
                else:
                    massages_to_send.append((current_socket, 'hello, ' + data))
        send_waiting_massages(wlist)


if __name__ == '__main__':
    main()