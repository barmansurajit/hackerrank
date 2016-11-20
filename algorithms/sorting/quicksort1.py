#!/bin/python

def partition(arr, n):
	p = arr[0]
	left, right, equal = [], [], []
	
	left  = [item for item in arr if item < p]
	right = [item for item in arr if item > p]
	equal = [item for item in arr if item == p]

	arr = left + equal + right
	print " ".join(str(i) for i in arr)

n = int(raw_input().strip())
arr = [int(i) for i in raw_input().strip().split()]
partition(arr, n)	