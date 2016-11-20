#!/bin/python

def fibonacci(t1, t2, n):
	array = [t1, t2]
	for i in range(2, n):
		item = array[i - 2] + array[i - 1] * array[i - 1]
		array.append(item)
	print array[n - 1]

if __name__ == '__main__':
	t1, t2, n = map(int, raw_input().strip().split())
	fibonacci(t1, t2, n)