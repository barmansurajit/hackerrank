#!/bin/python

def partition(arry):
	if len(arry) < 2:
		return arry
	else:
		p = arry[0]
		left, right, equal = [], [], []
		
		left  = [item for item in arry if item < p]
		right = [item for item in arry if item > p]
		equal = [item for item in arry if item == p]

		arry = partition(left) + equal + partition(right)
		
		print " ".join(str(i) for i in arry)
		return arry

n = int(raw_input().strip())
arr = [int(i) for i in raw_input().strip().split()]
partition(arr)	