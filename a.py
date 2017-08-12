import sys
import time
import datetime
import os

#
# f = open('test.text', 'a+')
# def write_data(i):
#     time.sleep(1)
#     s = str(datetime.datetime.now())
#     f.write(str(i) + ',' + s)
#     f.write('\n')
#     pass
#
# def get_num(fi):
#     s = fi.readlines()
#     if len(s) != 0:
#         l = s[-1]
#         if l == '\n':
#             i = 0
#         else:
#             i = int(l[0])
#         return i
#
#
# i = get_num(f) + 1
# while True:
#     write_data(i)
#     i += 1
#     pass
# --------------------------------------------------->
path = '/home/linux/python/mydir/'
f = open('all.text', 'a')
rootdir = os.listdir(path)

def get_dir_file(onedir):
    return os.listdir(path + onedir)
    pass

def get_file_content(filename):
    fileobj = open(filename, 'r')
    return fileobj.readlines()
    pass

def write_content(filename):
    fr = open(filename, 'r')
    f.writelines(fr.readlines())
    pass

for chiderdir in rootdir:
    if os.path.isfile(path + chiderdir):
        print "==========="
    else:
        print "---------"
        filename = get_dir_file(chiderdir)
        for chiderfile in filename:
            filepath = path + chiderdir + '/' + chiderfile
            write_content(filepath)
