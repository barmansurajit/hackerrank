#!/bin/python

def countsort(arry, n):
	cmap = {}
	value = 0
	while value in range(0,100):
		count = 0
		for i in arry:
			if value == i:
				count += 1
		cmap[value] = count
		value += 1
	
	a = []
	for k, v in cmap.items():
		index = 0
		while index in range(v):
			a.append(k)
			index += 1

	print " ".join(str(e) for e in a)

if __name__ == '__main__':
	n = int(raw_input().strip())
	arr = [int(i) for i in raw_input().strip().split()]
	countsort(arr, n)