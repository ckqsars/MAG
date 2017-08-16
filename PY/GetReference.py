#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @2016 R&D, CINS Inc. (cins.com)
#
# Author: chenkaiqi<ckqsars@sina.com>

import sys
import os
import time
sys.path.append('/usr/local/lib/python2.7/dist-packages/')

def readfilename(dir):                         #读取文件夹中的文件名
    filelist =[]
    
    for root,dirs,files in os.walk(dir):
        for file in files:
                filelist.append(file)
    #print filelist
    return filelist  

def ReadData(fr,delimiter):
    '''
    from the file read data 
    
    separator is  delimiter 
    '''
    
    for obj in fr:
        yield obj.strip().split(delimiter)

def GetIDdict(IDfile,delimiter):
    dict = {}
    fr = open(IDfile)
    lin = fr.readline()
    while(lin):
        lin = lin.strip().split('\t')
        dict[lin[0]] = int(lin[1])
        lin = fr.readline()
    return dict

def GetReference(indexfile,IDpath,outfile,delimiter = '\t'):
    fp = open(outfile,'w+') 
    filelist =  readfilename(IDpath)
    for file in filelist:
        IDfile  = IDpath + file
        dict = {}
        ReDict = {}
        dict = GetIDdict(IDfile,delimiter)
        
        print time.ctime()
        for index in dict:
            ReDict[index] = []
            
           
        fr = open(indexfile)
        lin = fr.readline()

        while(lin):            
            lin = lin.strip().split(delimiter)
            if len(lin) == 2:
                if lin[1] in ReDict:
                    index = lin[1]
                    ReDict[index].append(lin[0])
                    if len(ReDict[index]) == int(dict[index]) - 1:
                        fp.write(index+delimiter)
                        fp.write("{0}".format(delimiter.join(ReDict[index]))+'\n')
                        ReDict.pop(index)
            lin = fr.readline()
        print time.ctime()
        fr.close()
    fp.close()  
      
def main():
    indexfile = '/home/ckqsars/workspace/MAG/Data/PaperReferences.txt'
    IDpath = '/home/ckqsars/workspace/MAG/Data/2/'
    outfile = '/home/ckqsars/workspace/MAG/Data/Reference.txt'
    GetReference(indexfile,IDpath,outfile)
    
main()