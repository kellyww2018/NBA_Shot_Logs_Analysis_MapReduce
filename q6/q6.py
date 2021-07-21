#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 20:33:28 2020

@author: yaxinwan
"""
import sys
import pandas as pd
import numpy as np
from collections import defaultdict
DF=pd.read_csv('shot_logs.csv')
df_cz=DF.iloc[:,[11,16,8]]
df=df_cz[df_cz['SHOT_CLOCK'].isnull()==False]
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
dist_dict={}
cluster_loc=defaultdict(list)
centlst=defaultdict(list)
for i in range(len(df)):
    dist_dict={}
    data_point=df.iloc[i,:]
    for k in range(4):
        dist_dict[k]=np.linalg.norm(data_point-np.array(new_cent[k]))
    dist_dict_sorted=sorted(dist_dict.items(),key=lambda x: x[1])
    cluster_num=dist_dict_sorted[0][0]
    cluster_loc[cluster_num].append(i)
    centlst[cluster_num].append(data_point)

for i in ['james harden','chris paul', 'stephen curry','lebron james']:
    for j in range(4):
        temp1=DF.iloc[cluster_loc[j],:]
        temp2=temp1[temp1['player_name']==i]
        temp3=temp2[temp2['SHOT_RESULT']=='made']
        hit_rate=len(temp3)/len(temp2)
        print('In zone',j,',',i,'hit rate is:',hit_rate)    

