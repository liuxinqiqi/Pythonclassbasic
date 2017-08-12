
def fun(a,b):
    a = a + 1
    b = b + 1
    print a,b
    print id(a),id(b)


x,y = 5,6
a = x
b = y

fun(x,y)


print id(x),id(y)

print id(a),id(b)
