'''
좌표 정렬하기
'''

import sys

n = int(sys.stdin.readline())

coordis = []
for i in range(n):
    coordi = list(map(int, sys.stdin.readline().split()))
    coordis.append(coordi)

coordis.sort(key = lambda x: (x[0], x[1]))

for x, y in coordis:
    print(x, end=' ')
    print(y)