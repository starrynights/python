import socket
import sys

s = socket.socket()
#host = socket.gethostname()
host = "127.0.0.1"
port = 8888
s.connect((host,port))
while True:
    str = raw_input("Enter: ")
    s.send(str)
    print s.recv(1024)
