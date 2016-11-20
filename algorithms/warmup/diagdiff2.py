#!/bin/python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)
#print a

# first diagonal
fd = 0
for i in range(len(a)):
	fd += a[i][i]

#print fd

# second diagonal
sd = 0
y = len(a) -1
for i in range(len(a)):
	sd += a[i][y]
	y -= 1

#print sd

print abs((fd -sd))