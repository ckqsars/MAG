#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @2016 R&D, CINS Inc. (cins.com)
#
# Author: chenkaiqi<ckqsars@sina.com>

import sys
import os
import time
from optparse import OptionParser
sys.path.append('/usr/local/lib/python2.7/dist-packages/')

def str2lis(content, delimiter = '\t'):
    if isinstance(content, str):
    
        content = content.strip().split(delimiter)
        return content
    
def main():
    log = sys.stdout
    indexfile = '/home/ckqsars/workspace/MAG/Data/Paper_year.txt'
    #first = {}
    first = {'name':'1', 'time':1000}
    fr = open(indexfile)
    
    lin = fr.readline()
    while(lin):
        lin = str2lis(lin, delimiter = '\t')
        if int(lin[1]) < 2017:
            if int(lin[1]) > first['time']:
                first['time'] = int(lin[1])
                first['name'] = lin[0]
        lin = fr.readline()
    
    
    print first
    
main()   
