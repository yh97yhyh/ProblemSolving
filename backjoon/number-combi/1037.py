'''
약수
'''

import sys

nums = int(sys.stdin.readline())
factors = list(map(int, sys.stdin.readline().split()))
factors.sort()

print(factors[0] * factors[-1])