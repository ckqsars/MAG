#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @2016 R&D, CINS Inc. (cins.com)
#
# Author: chenkaiqi<ckqsars@sina.com>

import os

def main(path,outpath):
    
    #filelist = os.listdir(path)
    for i in range(1986,2008):
        fr = open(path+'/'+str(i)+'result.txt')
        fp = open(outpath+'/'+str(i)+'rank.txt','w+')
        dict = {}
        #frweight = open(weightpath+'/'+str(i)+'result.txt')
        for lin in fr:
            lin = lin.strip().split('\t')
            PaperID = lin[0]
            rank = lin[1]
            if rank != '0':
                dict[PaperID] = float(rank)
        fr.close()
        ranknum = sorted(dict.items(),key=lambda asd:asd[1], reverse=True)
        for content in ranknum:
            if content[1] != 1.0:
                fp.write('{0}\t{1}\n'.format(content[0],str(content[1])))
        fp.close()


    

if __name__ == "__main__":
    path = '/home/ckqsars/workspace/MAG/Data/weightresult4'
    outpath = '/home/ckqsars/workspace/MAG/Data/weightrank4'
    main(path,outpath)