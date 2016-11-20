#!/bin/python

def quicksort(arry, lo, hi):
	if lo < hi:
		p = partition(arry, lo, hi)
		print ' '.join(map(str, arry))
		quicksort(arry, lo, p - 1)
		quicksort(arry, p + 1, hi)

def partition(arry, lo, hi):
	pivot = arry[hi]
	i = lo

	for j in range(lo, hi):
		if arry[j] <= pivot:
			arry[j], arry[i] = arry[i], arry[j]
			i += 1
	arry[hi], arry[i] = arry[i], arry[hi]
	return i

if __name__ == '__main__':
	n = int(raw_input().strip())
	arr = [int(i) for i in raw_input().strip().split()]
	quicksort(arr, 0, n - 1)	