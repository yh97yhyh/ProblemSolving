'''
이항 계수
'''

import sys
from itertools import combinations

n, k = map(int, sys.stdin.readline().split())

nArr = ['1'] * n
nCk = list(combinations(nArr, k))
print(len(nCk))