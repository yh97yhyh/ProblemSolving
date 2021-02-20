'''
다리 놓기
'''

# 시간 초과
# import sys
# from itertools import combinations
#
# roof = int(sys.stdin.readline())
#
# for i in range(roof):
#     n, m = map(int, sys.stdin.readline().split())
#     mArr = ['1'] * m
#     mCn = list(combinations(mArr, n))
#     print(len(mCn))

import sys
import math

roof = int(sys.stdin.readline())

for i in range(roof):
    n, m = map(int, sys.stdin.readline().split())
    answer = math.factorial(m) // (math.factorial(n) * math.factorial(m-n))
    print(answer)