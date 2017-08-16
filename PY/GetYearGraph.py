#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @2016 R&D, CINS Inc. (cins.com)
#
# Author: chenkaiqi<ckqsars@sina.com>

import sys
import os
import time
import math
reload(sys)
sys.setdefaultencoding('utf-8')


def Getgraph(file,indexfile,outfile,year):
    yeardict = {}
    indexfr = open(indexfile)
    
    lin = indexfr.readline()
    while(lin):
        lin = lin.strip().split('\t')
        yeardict[lin[0]] = int(lin[1])
        lin = indexfr.readline()
    indexfr.close()
    yeardict['5E3BDA99'] = 1961
    #print yeardict
    fp = open(outfile,'w+')
    fr = open(file)
    lin = fr.readline()
    while(lin):
        lin = lin.strip().split('\t')
        if yeardict[lin[0]] <= year:
            weakValue = (-1.0*math.tanh(year-yeardict[lin[1]]-10)+3)/2
            influenceValue = math.exp(yeardict[lin[0]]-year)  
            fp.write(str(lin[0])+'\t'+str(lin[1])+'\t'+str(weakValue)+'\t'+str(influenceValue)+'\n')
        lin = fr.readline() 
    fp.close()
    fr.close()
    
    
def main():
    file = '/home/ckqsars/workspace/MAG/Data/5E3BDA99edges'
    indexfile = '/home/ckqsars/workspace/MAG/Data/5E3BDA99Year'
    for year in range(1961,2017):
        outfile = '/home/ckqsars/workspace/MAG/Data/6/'+str(year)+'5E3BDA99'
        print time.ctime()
        Getgraph(file,indexfile,outfile,year)
        
        
main()