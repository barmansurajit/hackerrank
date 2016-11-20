#!/bin/python

import sys

def rotateright(lst, num):
	if num > len(lst):
		num = num % len(lst)
		#print num
	lst[:] = lst[-num:] + lst[:-num]

def rotateleft(lst, num):
	if num > len(lst):
		num = num % len(lst)
		#print num	
	lst[:] = lst[num:] + lst[:num]

n,k,q = raw_input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = map(int,raw_input().strip().split(' '))

m = []
for a0 in xrange(q):
    m_temp = int(raw_input().strip())
    m.append(m_temp)

#print "a:", a
#print "m:", m
rotateright(a,k)
#print "a:", a

for item in range(len(m)):
	#print m[item]
	print a[m[item]]