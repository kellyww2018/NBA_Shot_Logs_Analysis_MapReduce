#!/usr/bin/env python
# coding: utf-8
import sys
import csv
import numpy as np
from collections import defaultdict
data=sys.stdin.readlines()
data= csv.reader(data)
next(data)
cent=sys.argv[1]
cent= cent.replace('[', '')
cent= cent.replace(']', '')
cent=cent.split(',')
new_cent=[]
center=[]
for i in cent:
    center.append(float(i))
    if len(center)==3:
        new_cent.append(center)
        center=[]
b=[11,16,8]
dist_dict={}
cluster_loc=defaultdict(list)
centlst=defaultdict(list)
i=0
for line in data:
    data_point=[line[j] for j in b]
    if '' in data_point:
        continue
    else:
        data_point=[float(data_point[k]) for k in range(3)]
    dist_dict={}
    for k in range(4):
        dist_dict[k]=np.linalg.norm(np.array(data_point)-np.array(new_cent[k]))
    dist_dict_sorted=sorted(dist_dict.items(),key=lambda x: x[1])
    cluster_num=dist_dict_sorted[0][0]
    cluster_loc[cluster_num].append(i)
    centlst[cluster_num].append(data_point)
    i+=1
for m in range(4):
    for n in centlst[m]:
        print('%s\t%s' %(m,n))
