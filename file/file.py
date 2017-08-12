import os
import shutil

# print dir(os)
#
# print "=================="
#
# print dir(os.path)
#
# print "==================="
#
# print dir(shutil)

print os.getcwd()

#os.remove('hold')

print os.path.isfile('file')
print os.path.isdir('file')
print os.path.exists('file')

print os.path.abspath(__file__)
print os.path.dirname(os.path.abspath(__file__))
print os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print os.path.getsize('file')

print os.path.join('/a/b/c','filename')

print os.listdir('.')

#os.system('ls -l')
#os.rename('csvfile1.xls','test.xls')
#os.mkdir('dir')

shutil.copyfile('file','filenew')
#shutil.move('a','b')

#shutil.copy('a','b')
