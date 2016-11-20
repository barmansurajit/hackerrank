#!/bin/python

def insertionSort(arr, n):
	for i in range(1, n):
		val = arr[i]
		j = i

		while j > 0 and arr[j - 1] > val:
			arr[j] = arr[j - 1]
			j -= 1			
		arr[j] = val
		print " ".join(map(str, arr))

n = int(raw_input().strip())
arr = [int(i) for i in raw_input().strip().split()]
insertionSort(arr, n)