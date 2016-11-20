#!/bin/python


n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))

#print arr

# Value to be inserted to make the list sorted
v = arr[n - 1]
j = 0

while n > 1:
	if arr[n - 2] > v:
		arr[n - 1] = arr[n - 2]
		strg = " ".join(str(e) for e in arr)
		print strg
	else:
		arr[n -1] = v
		j = 1
		break
	n -= 1

if not j:	
	arr[0] = v
strg = " ".join(str(e) for e in arr)
print strg
