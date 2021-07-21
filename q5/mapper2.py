#!/usr/bin/env python
# coding: utf-8
import sys
for line in sys.stdin:
    line=line.strip()
    line=line.split("\t")
    player_defender=line[0].split(',')
    player=player_defender[0][1:]
    defender=player_defender[1][:-1]
    hit_rate=line[1]
    print ('%s\t%s\t%s' %(player,defender,hit_rate))



