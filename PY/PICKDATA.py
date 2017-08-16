#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @2016 R&D, CINS Inc. (cins.com)
#
# Author: chenkaiqi<ckqsars@sina.com>

def ReadData(fr,delimiter):
    '''
    from the file read data 
    
    separator is  delimiter 
    '''
    
    for obj in fr:
        yield obj.strip().split(delimiter)

def main(path,weightpath,pickpath):
    for i in range(1986,2008):
        print i
        rankDict = {}
        weightRankDict = {}
        
        rankFr = open(path+'/'+str(i)+'rank.txt')
        rankWeightFr = open(weightpath+'/'+str(i)+'rank.txt')
        fp = open(pickpath+'/'+str(i)+'pickrank.txt','w+')
        rankData = list(ReadData(rankFr,'\t'))
        rankWeightData = list(ReadData(rankWeightFr,'\t'))
        
        for lin in rankWeightData:
            weightRankDict[lin[0]] = int(0)
            
        for lin in rankData:
            if lin[0] in weightRankDict:
                fp.write("{0}\t{1}\n".format(lin[0],lin[1]))
        
        fp.close()
    
if __name__=="__main__":
    path = '/home/ckqsars/workspace/MAG/Data/rank'
    weightpath = '/home/ckqsars/workspace/MAG/Data/weightrank4'
    pickpath = '/home/ckqsars/workspace/MAG/Data/pickrank4'
    main(path,weightpath,pickpath)