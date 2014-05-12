import socket

s = socket.socket()
host = socket.gethostname()
port = 9999
s.bind(('192.168.109.128',port))
s.listen(5)
while True:
    c,addr = s.accept()
    print "client addr is " + addr
    c.send("hello")
    c.close()
