#!/bin/python

def format(S):
	i = 0
	arr = []
	while i in range(len(S)):
		try:
			if i == 0:
				arr.append(S[i].capitalize())
			elif ('.' in S[i] or '?' in S[i] or '!' in S[i]) and S[i + 1] is not None:
				arr.append(S[i])
				arr.append(S[i + 1].capitalize())
				i += 1
			else:
				arr.append(S[i])
			i += 1
		except IndexError:
			arr.append(S[i])
			i += 1
	print ' '.join(str(item) for item in arr)

if __name__ == '__main__':
	s = raw_input().strip().split()
	format(s)