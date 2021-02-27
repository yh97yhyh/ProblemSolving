'''
팩토리얼 0의 개수
'''

import sys

n = int(sys.stdin.readline())

fct = 1
for i in range(1, n+1):
    fct *= i
fct = list(str(fct))
fct.reverse()

for i in range(len(fct)):
    if fct[i] != '0':
        print(i)
        break