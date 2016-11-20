#!/bin/python

def countsort(arry, n):
	cmap = {}
	v = 0
	while v in range(0,100):
		count = 0
		for i in arry:
			if v == i:
				count += 1
		cmap[v] = count
		v += 1
	print " ".join(str(e) for e in cmap.values())

if __name__ == '__main__':
	n = int(raw_input().strip())
	arr = [int(i) for i in raw_input().strip().split()]
	countsort(arr, n)