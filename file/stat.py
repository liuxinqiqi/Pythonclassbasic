import os
import time

filename = raw_input("file name:")

file_stat = os.stat(filename)

print file_stat

print time.localtime(file_stat.st_ctime)
