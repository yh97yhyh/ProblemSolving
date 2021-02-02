'''
문자열 반복
'''

import sys

n = int(sys.stdin.readline())

for i in range(n):
    num, string = sys.stdin.readline().split()
    num = int(num)
    for s in string:
        for j in range(num):
            print(s, end='')
    print()