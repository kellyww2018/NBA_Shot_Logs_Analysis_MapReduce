#!/usr/bin/env python
# coding: utf-8

import sys
import numpy as np
from collections import defaultdict
cent_dict=defaultdict(list)
for line in sys.stdin:
    line=line.strip()
    line=line.split('\t')
    cent_num=int(line[0])
    data_point=line[1]
    data_point = [float(x) for x in data_point[1:-1].split(',')]
    cent_dict[cent_num].append(data_point)
cent=[]
for i in range(4):
    centarray=np.vstack(cent_dict[i])
    new_cent=np.mean(centarray,axis=0)
    new_cent=[round(i,3) for i in new_cent]
    cent.append(new_cent)
a=str(cent)
print(a.replace(' ',''))
