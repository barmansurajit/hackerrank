#!/bin/python
import runtimeis, runtimeqs

if __name__ == '__main__':
	n = int(raw_input().strip())
	arr1 = [int(i) for i in raw_input().strip().split()]
	arr2 = arr1[:]
	runtimeqs.quicksort(arr1, 0, n - 1)
	runtimeis.insertionSort(arr2, n)
	print runtimeis.getshifts() - runtimeqs.getswaps()