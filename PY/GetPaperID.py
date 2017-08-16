#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @2016 R&D, CINS Inc. (cins.com)
#
# Author: chenkaiqi<ckqsars@sina.com>

import sys
import os
sys.path.append('/usr/local/lib/python2.7/dist-packages/')

def GetID(file,outfile):
    fr = open(file)
    dict = {}
    lin = fr.readline()
    while(lin):
        lin = lin.strip().split('\t')
        RID = lin[1]
        if RID not in dict:
            dict[RID] = 1
                #except:
                    #print ID,len(lin)
        lin = fr.readline()
    fr.close()
    fr = open(file)
    lin =  fr.readline()
    while(lin):
        lin = lin.strip().split('\t')
        ID = lin[1]
        dict[ID] = dict[ID] + 1
        lin = fr.readline()
    print len(dict)
    fp = open(outfile,'w+')
    for ID in dict:
        fp.write(ID+'\t'+str(dict[ID])+'\n')
    fp.close() 

def main():
    file = '/home/ckqsars/workspace/MAG/Data/PaperReferences.txt'
    outfile = '/home/ckqsars/workspace/MAG/Data/PaperID.txt'
    GetID(file,outfile)
    
    
main()