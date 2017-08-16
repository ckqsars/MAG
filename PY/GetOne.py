#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @2015 R&D, CINS Inc. (cins.com)
#
# Author: chenkaiqi<ckqsars@sina.com>

import networkx as nx
import sys
import os
import json
import time

reload(sys)
sys.setdefaultencoding("utf-8")

def GetIDdict(IDfile,delimiter):
    dict = {}
    fr = open(IDfile)
    lin = fr.readline()
    while(lin):
        lin = lin.strip().split('\t')
        dict[lin[0]] = int(lin[1])
        lin = fr.readline()
    return dict

def readfilename(dir):                         #读取文件夹中的文件名
    filelist =[]
    
    for root,dirs,files in os.walk(dir):
        for file in files:
                filelist.append(file)
    #print filelist
    return filelist   

def GetOne(indexfile,outpath, filename, delimiter):
    IDdict = GetIDdict(indexfile, delimiter)
    IDlen = len(IDdict)
    splitlen = IDlen /100 + 1
    count = 0
    number = 0
    for index in IDdict:
        if count == 0:
            print number
            outfile = outpath+filename+str(number)
            fp = open(outfile,'w+')
        fp.write(str(index)+delimiter+str(IDdict[index])+'\n')
        count = count + 1
        if count == splitlen:
            count = 0
            number = number + 1
            fp.close()
    fp.close()


def main():
    indexfile = '/home/ckqsars/workspace/MAG/Data/PaperID.txt'
    outpath = '/home/ckqsars/workspace/MAG/Data/2/'
    filename = 'PaperID_'
    delimiter = '\t'
    GetOne(indexfile,outpath, filename, delimiter)

main()