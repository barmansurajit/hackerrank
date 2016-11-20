#!/bin/python

shifts = 0
swaps = 0

def insertionSort(arr, n):
	global shifts
	for i in range(1, n):
		val = arr[i]
		j = i

		while j > 0 and arr[j - 1] > val:
			arr[j] = arr[j - 1]
			shifts += 1
			j -= 1
		arr[j] = val
		#print " ".join(map(str, arr))

def getshifts():
	return shifts

def quicksort(arry, lo, hi):
	if lo < hi:
		p = partition(arry, lo, hi)
		#print ' '.join(map(str, arry))
		quicksort(arry, lo, p - 1)
		quicksort(arry, p + 1, hi)

def partition(arry, lo, hi):
	global swaps
	pivot = arry[hi]
	i = lo

	for j in range(lo, hi):
		if arry[j] <= pivot:
			arry[j], arry[i] = arry[i], arry[j]
			i += 1
			swaps += 1
	arry[hi], arry[i] = arry[i], arry[hi]
	swaps += 1
	return i

def getswaps():
	return swaps

if __name__ == '__main__':
	n = int(raw_input().strip())
	arr1 = [int(i) for i in raw_input().strip().split()]
	arr2 = arr1[:]
	quicksort(arr1, 0, n - 1)
	insertionSort(arr2, n)
	print getshifts() - getswaps()
