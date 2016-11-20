#!/bin/python

import sys


a0,a1,a2 = raw_input().strip().split(' ')
alice = [int(a0),int(a1),int(a2)]
b0,b1,b2 = raw_input().strip().split(' ')
bob = [int(b0),int(b1),int(b2)]

alice_score = bob_score = 0

for i in xrange(3):
    if alice[i] > bob[i]:
        alice_score += 1
    elif alice[i] < bob[i]:
        bob_score += 1

print alice_score, bob_score
