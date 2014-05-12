import socket

s = socket.socket()
host = socket.gethostname()
port = 8889
s.connect(('192.168.109.128',port))
#s.connect((host,port))
print s.recv(1024)
