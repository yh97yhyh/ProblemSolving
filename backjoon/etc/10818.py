'''
최소, 최대
'''

import sys

n = int(sys.stdin.readline())
numArr = list(map(int, sys.stdin.readline().split()))
numArr.sort()

print('{} {}'.format(numArr[0], numArr[n-1]))