class Magic1(object):
    def __init__(self):
        print "__init__......."

    def __new__(cls):
        print "__new__ ......"
        return super(Magic1,cls).__new__(cls)


    def __call__(self,a):
        print a

    def __del__(self):
        print "__del__........"

m = Magic1()
m("This is call")

del m

print "over"
