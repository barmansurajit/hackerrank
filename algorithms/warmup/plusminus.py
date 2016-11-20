#!/bin/python
from __future__ import division

n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))

#arr = list()
#for i in range(n):
#  a_temp = int(raw_input().strip())
#  arr.append(a_temp)


pos = [item for item in arr if item > 0]
neg = [item for item in arr if item < 0]
zer = [item for item in arr if item == 0]



print len(pos)/len(arr)
print len(neg)/len(arr)
print len(zer)/len(arr)

