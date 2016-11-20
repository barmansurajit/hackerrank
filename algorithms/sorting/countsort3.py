#!/bin/python

if __name__ == '__main__':
	n = int(raw_input().strip())
	d = dict()
	for _ in range(n):
		key,value = raw_input().strip().split()
		if key in d.keys():
			d[key] += 1
		else:
			d[key] = 1

	arr = []
	result = 0
	for i in range(100):
		if str(i) in d.keys():
			result += d[str(i)]
			arr.append(result)
		else:
			arr.append(result)
	print " ".join(str(e) for e in arr)