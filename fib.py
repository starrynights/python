class Fib:
    def __init__(self,max):
        self.a = 0
        self.b = 1
        self.n = 0
        self.max = max

    def next(self):
        while self.n < self.max:
            r = self.a
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration()

    def __iter__(self):
        return self

#fib = Fib(10)
for i in Fib(10):
    print i
