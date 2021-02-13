'''
벌집
'''

import sys

n = int(sys.stdin.readline())

first = 2
last = 7
cnt = 2

if n == 1:
    print(n)
elif 2 <= n <= 7:
    print(2)
else:
    while True:
        first = last + 1 # 범위의 처움
        last = last + 6*cnt # 범위의 끝
        if first <= n <= last:
            # print(first, last)
            print(cnt+1)
            break
        cnt += 1