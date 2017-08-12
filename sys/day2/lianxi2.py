#!/usr/bin/python

import os 
def linkFilesInDirs(rootDir,outputFile):
    path = '{}/{}'.format(rootDir,outputFile)
    fw = open(path,'a+')
    for dirName in os.listdir(rootDir):
        if os.path.isdir("{}/{}".format(rootDir,dirName)):
            print 'process in dir:%s'%dirName
            for fileName in os.listdir('{}/{}'.format(rootDir,dirName)):
                if os.path.isfile('{}/{}/{}'.format(rootDir,dirName,fileName)):
                    fr = open(os.path.join(rootDir,dirName,fileName),'r')
                    for eachLine in fr:
                        fw.write(eachLine)

                    fr.close()
    fw.close()

linkFilesInDirs('myDir','new.txt')
