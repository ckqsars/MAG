#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @2016 R&D, CINS Inc. (cins.com)
#
# Author: chenkaiqi<ckqsars@sina.com>

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def main():
    indexfile = '/home/ckqsars/workspace/MAG/Data/Paper_year.txt'
    goalfile = '/home/ckqsars/workspace/MAG/Data/5E3BDA99edges'
    outfile = '/home/ckqsars/workspace/MAG/Data/5E3BDA99Year'
    fr = open(goalfile)
    lin = fr.readline()
    dict = {}
    while(lin):
        lin = lin.strip().split('\t')
        if lin[0] not in dict:
            dict[lin[0]] = 0
        lin = fr.readline()
    fr.close()
    fr1 = open(indexfile)
    fp = open(outfile,'w+')
    lin = fr1.readline()
    #dict = {}
    while(lin):
        lin = lin.strip().split('\t')
        #print lin[0]
        if lin[0]  in dict:
            fp.write(str(lin[0])+'\t'+str(lin[1])+'\n')
        lin = fr1.readline()
    fr1.close()
    fp.close()
    
main()