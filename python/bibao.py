def out():
    a = 1
    def inner():
        print a
        print "I'm inner"
    return inner

f = out()
f()
