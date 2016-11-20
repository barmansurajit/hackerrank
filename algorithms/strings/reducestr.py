#!/bin/python

def reduce(S):
	print S
	i = 1

	while i in range(len(S)):
		if S[i] == S[i - 1]:
			S = S[0:i-1] + S[i+1:]
		i += 1
	
	if len(S) == 0:
		print 'Empty String'
	else:
		print S

if __name__ == '__main__':
	s = raw_input().strip()
	reduce(s)