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

def GetDict(file,dict,indexContent):
    fr = open(file)
    lin = fr.readline()
    while(lin):
            lin = lin.strip().split('\t')
            if lin[1] == indexContent:
                dict[indexContent][lin[0]] = {}
            lin = fr.readline()
    fr.close()
    return dict

def GetOne(file,indexContent,path):
    #fr = open(file)
    #lin = fr.readline()
    dict = {}
    dict[indexContent] = {}
    
    t = 0
    print '1'
    while(t < 1):
        if t == 0:
            fp = open(path+str(t),'w+')
            print '1'
            list = [indexContent]
        for indexContent in list:
            dict = GetDict(file, dict, indexContent)
            if len(dict[indexContent]) == 0:
                break
            fp.write(str(indexContent))
            for index in dict[indexContent]:
                fp.write('\t'+str(index))
        
        fp.write('\n')
        fp.close()
        t = t + 1
        
    
        
                
            


def main():
    file = '/home/ckqsars/workspace/MAG/Data/PaperReferences.txt'
    indexContent = '5E3BDA99'
    path = '/home/ckqsars/workspace/MAG/Data/2/'
    #dict = {}
    GetOne(file,indexContent,path)

main()