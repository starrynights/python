import socket
import sys
import threading


class deal_thread(threading.Thread):
    def __init__(self, conn, addr):
        threading.Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        self.thread_stop = False

    def run(self):
        while not self.thread_stop:
            try:
                str = self.conn.recv(1024)
            except socket.error, msg:
                print "Receive msg failed, Error code: " + str(msg[0]) + " ,Error message: " + msg[1]
                self.stop()
            if not str:
                self.stop()
            else:
                id = self.ident
                count = threading.activeCount()
                print count, " Thread ", id, " Get conn from ", self.addr, " : ", str
                self.conn.send("hello from server")
    
    def stop(self):
        self.thread_stop = True

def deal_conn(conn, addr):
    thread = deal_thread(conn, addr)
    thread.start()

if __name__ == '__main__':
    host = "127.0.0.1"
    port = 8888
    try:
        s = socket.socket()
    except socket.error, msg:
        print "Failed to create socket, Error code: " + str(msg[0]) + " , Error message: " + msg[1]
        sys.exit()
    print "Socket created successfully"

    s.bind((host,port))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        deal_conn(conn, addr)
    s.close()
