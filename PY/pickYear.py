#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @2016 R&D, CINS Inc. (cins.com)
#
# Author: chenkaiqi<ckqsars@sina.com>

import sys


reload(sys)
sys.setdefaultencoding( "utf-8" )

def ReadData(fr,delimiter):
    '''
    from the file read data 
    
    separator is  delimiter 
    '''
    
    for obj in fr:
        yield obj.strip().split(delimiter)

def pickYear(indexfile, goalfile, outfile,delimiter):
    dict =  {}
    fr = open(indexfile)
    #data = ReadData(fr, delimiter)
    lin = fr.readline()
    while(lin):
        lin = lin.strip().split(delimiter)
        try:
            dict[lin[1]] = 0
        except:
            print len(dict)
            break
        lin = fr.readline()
    fr.close()
    frgoal = open(goalfile)
    lin = frgoal.readline()
    while(lin):
        lin = lin.strip().split(delimiter)
        if lin[0] in dict:
            dict[lin[0]] = lin[3]
        lin = frgoal.readline()
    frgoal.close()
    fp =open(outfile,'w+')
    temp = 0
    for index in dict:
        if dict[index] == 0:
            temp = temp + 1
        fp.write(index+delimiter+str(dict[index])+'\n')
    fp.close()
    print temp
    

def main():
    indexfile = '/home/ckqsars/workspace/MAG/Data/PaperReferences.txt'
    goalfile = '/home/ckqsars/workspace/MAG/Data/Papers.txt'
    outfile = '/home/ckqsars/workspace/MAG/Data/Paper_year_2.txt'
    delimiter = '\t'
    pickYear(indexfile, goalfile, outfile,delimiter)
    
main()