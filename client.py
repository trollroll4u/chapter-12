# -*- coding: utf-8 -*-
import socket


def main():
    my_socket = socket.socket()
    my_socket.connect(('127.0.0.1', 23))
    my_socket.send(raw_input())
    my_socket.close()

if __name__ == '__main__':
    main()