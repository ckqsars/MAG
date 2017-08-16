#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @2015 R&D, CINS Inc. (cins.com)
#
# Author: chenkaiqi<ckqsars@sina.com>

import networkx as nx
import sys
import math
import os
import matplotlib.pyplot as plt
import pandas as pd
import json
import time

reload(sys)
sys.setdefaultencoding("utf-8")

def str2lis(content, delimiter = '\t'):
    if isinstance(content, str):
    
        content = content.strip().split(delimiter)
        return content
    
def GetGraph(datafile,indexContent,outfile,oldindexContent):
    newDictContent = {}
    newIndexContent = []
    dictContent = {}
    for index in indexContent:
        dictContent[index] = 0
    fr = open(datafile)
    lin = fr.readline()
    while(lin):
        lin = str2lis(lin, delimiter = '\t')
        if lin[0] in dictContent:
            for i in range(len(lin)):
                if i != 0:
                    outfile.write(str(lin[i])+'\t'+str(lin[0])+'\n')
                    if lin[i] not in newIndexContent and lin[i] not in oldindexContent:
                        newDictContent[lin[i]] = 1
                        oldindexContent[lin[i]] = 0
        lin = fr.readline()
    for index in newDictContent:
        newIndexContent.append(index)
    
    fr.close()
    
    return newIndexContent,oldindexContent                
                
        

    
def main():
    file = '/home/ckqsars/workspace/MAG/Data/Reference.txt'
    outfile = '/home/ckqsars/workspace/MAG/Data/5E3BDA99edges'
    fp = open(outfile,'w+')
    indexContent = ['5E3BDA99']
    oldindexContent = {}
    oldindexContent['5E3BDA99'] = 0
    a = 1
    while(indexContent):
        print time.ctime()
        indexContent,oldindexContent = GetGraph(file,indexContent,fp,oldindexContent)
        a = a + 1 
        print len(indexContent)
        
            
    fp.close()
    print len(indexContent)
    
        
main()