#!/usr/bin/env python
# coding: utf-8

import sys
from collections import defaultdict
from operator import itemgetter
shot_count=defaultdict(dict)
for line in sys.stdin:
    line = line.strip()
    line=line.split('\t')
    player_defender=line[0]
    made_num=line[1]
    count=line[2]
    made_num=int(made_num)
    count=int(count)
    shot_count[player_defender]['shot']=shot_count[player_defender].get('shot',0)+made_num
    shot_count[player_defender]['total']=shot_count[player_defender].get('total',0)+count
for k,v in shot_count.items():
    hit_rate=float(v['shot'])/float(v['total'])
    hit_rate=round(hit_rate,4)
    print('%s\t%s'% (k,hit_rate))
