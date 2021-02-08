'''
블랙잭
'''

import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())

cards = list(map(int, sys.stdin.readline().split()))

combis = list(permutations(cards, 3))
# print(combis)

max = 0
for combi in combis:
    tmp = sum(combi)
    if tmp > max and tmp <= m:
        max = tmp

print(max)