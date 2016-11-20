#!/bin/python

import sys


n = int(raw_input().strip())
#a = []
#for a_i in xrange(n):
#    a_temp = map(int,raw_input().strip().split(' '))
#    a.append(a_temp)
#print a

dsumleft = 0
dsumright = 0

for i in range(n):
   matrixRow = raw_input().split()
   dsumleft += int(matrixRow[i])
   dsumright += int(matrixRow[-(i+1)])

print -1 * (dsumleft - dsumright)
