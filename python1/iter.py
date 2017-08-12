
class TestIter(object):
    def __init__(self,a):
        self.a = a

    def __iter__(self):
        return self

    def next(self):
        self.a += 1
        if self.a > 10:
            raise
        return self.a ** 2


n =  TestIter(2)
print n.next()
print n.next()
print n.next()
print n.next()
