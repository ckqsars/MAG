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

def main(pickRankPath,weightRank2Path,errorRank2Path):
    for i in range(1986,2008):
        print i
        rankDict = {}
        weightRankDict = {}
        
        rankPickFr = open(pickRankPath+'/'+str(i)+'pickrank.txt')
        rankWeightFr = open(weightRank2Path+'/'+str(i)+'rank.txt')
        fp = open(errorRank2Path+'/'+str(i)+'errorrank.txt','w+')
        
        rankPickData = list(ReadData(rankPickFr,'\t'))
        for num in range(len(rankPickData)):
            rankDict[rankPickData[num][0]] = num
         
        rankWeightData = list(ReadData(rankWeightFr,'\t'))   
        for num in range(len(rankWeightData)):
            weightRankDict[rankWeightData[num][0]] = num
        
        
        
        if len(rankPickData) == len(rankWeightData):
            for index in rankDict:
                if rankDict[index] != weightRankDict[index]:
                    fp.write("{0}\t{1}\t{2}\n".format(index,str(rankDict[index]),str(weightRankDict[index])))
        else:
            print len(rankPickData), len(rankWeightData) 
        fp.close()
    
if __name__=="__main__":
    pickRankPath = '/home/ckqsars/workspace/MAG/Data/pickrank'
    weightRank2Path = '/home/ckqsars/workspace/MAG/Data/weightrank4'
    errorRank2Path = '/home/ckqsars/workspace/MAG/Data/errorrank4'
    main(pickRankPath,weightRank2Path,errorRank2Path)
    