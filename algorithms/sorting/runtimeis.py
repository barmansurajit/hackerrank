#!/bin/python

shifts = 0

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

if __name__ == '__main__':
	n = int(raw_input().strip())
	arr = [int(i) for i in raw_input().strip().split()]
	insertionSort(arr, n)
	print getshifts()
	#print " ".join(map(str, arr))