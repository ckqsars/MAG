#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @2016 R&D, CINS Inc. (cins.com)
#
# Author: chenkaiqi<ckqsars@sina.com>

import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def countdegree(file):
    fr = open(file)
    lin = fr.readline()
    DictInNode = {}
    DictOutNode = {}
    Degree = 0
    while(lin):
        lin = lin.strip().split('\t')
        if lin[0] not in DictInNode:
            DictInNode[lin[1]] = 0
        if lin[1] not in DictOutNode:
            DictOutNode[lin[0]] = 0
        Degree = Degree + 1
        lin = fr.readline()
        
    numberLeaf = 0
    for index in DictOutNode:
        if index not in DictInNode:
            numberLeaf = numberLeaf + 1
    numberNode = len(DictInNode)+numbereaf
    
    
    print "the number of leaf is "+str(numberLeaf)    
    print "the number of out nodes is "+str(len(DictOutNode))    
    print "the sum degree is "+str(Degree)
    print "the number of input nodes is "+str(len(DictInNode))
    print "the average degree is "+str(1.0*Degree/numberNode)
    

def main():
    file = "/home/ckqsars/workspace/MAG/Data/5E3BDA99edges"
    countdegree(file)
    
main()