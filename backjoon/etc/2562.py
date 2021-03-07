'''
최댓값
'''

import sys

nums = []
for i in range(9):
    n = int(sys.stdin.readline())
    nums.append(n)

print(max(nums))
print(nums.index(max(nums))+1)