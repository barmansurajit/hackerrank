#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

total = reduce(lambda total, arr: total + arr, arr)

print total
