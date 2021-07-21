#!/usr/bin/env python
# coding: utf-8
import sys
from collections import defaultdict

shot_count=defaultdict(dict)
for line in sys.stdin:
    line = line.strip()
    line=line.split('\t')
    player=line[0]
    defender=line[1]
    hit_rate=line[2]
    shot_count[player][defender]=hit_rate
for k,v in shot_count.items():
    shot_count[k]=sorted(v.items(), key=lambda x:x[1])
    for i in shot_count[k]:
        print('%s\t%s\t%s' % (k,i[0],i[1]))


