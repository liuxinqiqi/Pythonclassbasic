try:
    f = open('default.png','r')
    f1 = open('/home/linux/djangosite/booksite/static/default.png','w')
except:
    print "open failed"

while True:
    s = f.read(12)
    if not s:
        break
    f1.write(s)
