import threading


class Producter(threading.Thread):
    def __init__(self, name):
        super(Producter,self).__init__()
        self.t_name = name
    def run(self):
        global x
        con.acquire()
        if x < 5 :
            print "producting..."
            for i in range(1,5):
                x += 1
            print "now x is ", x
            con.notifyAll()
        else:
            con.wait()
        con.release()

class Consumer(threading.Thread):
    def __init__(self,name):
        super(Consumer,self).__init__()
        self.t_name = name
    def run(self):
        global x
        con.acquire()
        if x > 0:
            print "consuming..."
            x -= 1
            print "now x is ", x
            con.notifyAll()
        else:
            con.wait()
        con.release()

con = threading.Condition()
x = 1
print "start consumer..."
c = Consumer('consumer')
c.start()
print "start producer..."
p = Producter('producer')
p.start()

#p.join()
#c.join()
print x
