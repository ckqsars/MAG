#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @2016 R&D, CINS Inc. (cins.com)
#
# Author: chenkaiqi<ckqsars@sina.com>

def GetTheDegree(path):
    
    paperDict = {}
    
    for i in range(1986,2007):
        fr = open(path+str(i)+'5E3BDA99')
        for lin in fr:
            lin = lin.strip().split('\t')
            if lin[1] not in paperDict:
                paperDict[lin[1]] = {}
            paperDict[lin[1]][i] = paperDict[lin[1]].get(i,0) + 1
    