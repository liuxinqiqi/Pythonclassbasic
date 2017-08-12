#!/usr/bin/python
#coding=utf-8

import MySQLdb
import getpass

password = getpass.getpass("Please input your password:")

#打开数据库链接
try:
    db = MySQLdb.connect('localhost','root',password,'stu')
except MySQLdb.OperationalError:
    exit(1)

#获取数据库游标
cursor = db.cursor()

try:
    cursor.execute("select * from student")
    # data = cursor.fetchone()
    # print data
    # data = cursor.fetchone()
    # print data
    # data = cursor.fetchone()
    # print data
    # data = cursor.fetchone()
    # print data
    # data = cursor.fetchone()
    # print data
    # data = cursor.fetchone()
    # print data

    data = cursor.fetchall()
    #print data

    for i in cursor.description:
        print i[0],

    print ""

    for row in data:
        for i in row:
            print i,
        print ""

except:
    print "Error:unable to fecth data"

db.close()
