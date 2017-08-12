class DictDemo(object):
    def __init__(self,key,value):
        self.dict = {}
        self.dict[key] = value

    def __getitem__(self,key):
        return self.dict[key]

    def __setitem__(self,key,value):
        self.dict[key] = value

    def __len__(self):
        return len(self.dict)


d = DictDemo('key0',1)

d['key1'] = 2
d[1] = 3

print d[1]

print len(d)
