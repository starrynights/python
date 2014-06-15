import threading
import sys

myLock = threading.RLock()
num = 0

class myThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.t_name = name
    def run(self):
        global num
        while True:
            myLock.acquire()
            print "Thread(%s) locked, num: %d" % (self.t_name, num)
            if (num >10):
                myLock.release()
                print "Thread(%s) released, num: %d" % (self.t_name, num)
                break
            num += 1
            print "Thread(%s) released, num: %d" % (self.t_name, num)
            myLock.release()

def test():
    thread1 = myThread('A')
    thread2 = myThread('B')
    thread1.start()
    thread2.start()

if __name__ == '__main__':
    test()

