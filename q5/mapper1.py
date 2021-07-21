#!/usr/bin/env python
# coding: utf-8
import sys
for line in sys.stdin:
    line=line.strip()
    line=line.split(",")
    player=line[-2]
    defender_surname=line[15][1:]
    defender_given=line[16][:-1]
    defender=defender_surname+defender_given
    if line[14]=='made':
        result=1
    else:
        result=0
    print ('%s\t%s\t%s' %((player,defender),result,1))

