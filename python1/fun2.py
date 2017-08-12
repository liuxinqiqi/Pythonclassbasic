def fun(a):
    a[1] = 1000
    print a
    print id(a)

l = [1,2,3,4]

#l1 = l[:]

fun(l1)

print "========================="
print id(l)

print l
