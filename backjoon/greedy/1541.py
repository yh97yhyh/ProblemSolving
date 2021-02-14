'''
잃어버린 괄호
'''

import sys

arr = sys.stdin.readline().strip().split('-')

sum = 0
for i in arr[0].split('+'): # -가 없다 (+만 있다)
    sum += int(i)
for i in arr[1:]:
    for j in i.split('+'):
        sum -= int(j)

print(sum)