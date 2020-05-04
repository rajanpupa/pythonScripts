#!/usr/bin/python3

import socket

# sepcify ipv4 and TCP connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

host = "137.74.187.102"
port = 443

def portScanner(port):
    print("scanning port ", port)
    if s.connect_ex((host, port)):
        print("The port is closed")
    else :
        print("The port is open")
    s.close()

portScanner(port)


