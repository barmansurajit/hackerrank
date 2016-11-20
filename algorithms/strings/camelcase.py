#!/bin/python

def countwords(S):
	count = sum(1 for s in S if s.isupper())
	print count + 1

if __name__ == '__main__':
	s = raw_input().strip()
	countwords(s)