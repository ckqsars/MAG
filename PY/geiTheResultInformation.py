#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @2016 R&D, CINS Inc. (cins.com)
#
# Author: chenkaiqi<ckqsars@sina.com>


import matplotlib.pyplot as plt

def PlotGraph(years,weights,x_label,y_label,paper):
    
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    
    plt.title('weigths of'+paper)
    plt.plot(years,weights,'r')
    plt.plot(years,weights,'b*')
    plt.show()
    
def GetGraphOfPaper(path):
    
    paperDict = {}
    
    for i in range(1986,2007):
        fr = open(path+str(i)+'result.txt')
        for lin in fr:
            lin = lin.strip().split('\t')
            if lin[0] not in paperDict:
                paperDict[lin[0]] = {}
            paperDict[lin[0]][i] = float(lin[1])
    
    
    max = 0
    for index in paperDict:
        if max <= len(paperDict[index]):
            max =len(paperDict[index])
            maxPaper = index
            
    print max
    
    maxPaper = '7CBCF338'
    years = []
    weights=[]
    for year in paperDict['7CBCF338']:
        print paperDict[maxPaper][year],year 
        years.append(int(year))
        weights.append(float(paperDict[maxPaper][year]))
    PlotGraph(years,weights,'years','weights',maxPaper)
    
def main(path):
    GetGraphOfPaper(path)
    
if __name__ == '__main__':
    path = '/home/ckqsars/workspace/MAG/Data/weightresult4/'
    main(path)