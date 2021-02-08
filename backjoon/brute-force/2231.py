'''
분해합
'''

import sys

n = int(sys.stdin.readline())

def sum_digit(num):
    num = str(num)
    sumNum = 0
    for digit in num:
        sumNum = sumNum + int(digit)
    return sumNum

for i in range(n):
    temp = i + sum_digit(i)
    if temp == n:
        print(i)
        break
    if i == n-1: # 답이 없을 때
        print(0)