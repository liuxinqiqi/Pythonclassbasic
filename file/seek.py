f = open('file','r+')

s = f.read(6)

print f.tell()
f.seek(6)
#f.seek(6,1)
#f.seek(-7,2)
print f.read(6)
