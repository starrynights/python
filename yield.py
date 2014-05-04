def test():
    print "step 1"
    m = yield '5'
    print "step 2", m
    d = yield 2
    print "step 3", d

t = test()
t.next()
t.next()
t.next()
