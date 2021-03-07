'''
숫자의 개수
'''

import sys

num = 1
for i in range(3):
    num = num * (int(sys.stdin.readline()))
num = str(num)

arr = [0 for i in range(10)]

for i in range(10):
    cnt = num.count(str(i))
    arr[i] = arr[i] + cnt
    print(arr[i])