'''
숫자의 합
'''

import sys

n = int(sys.stdin.readline())
nums = list(sys.stdin.readline())
nums.pop()
nums_int = list(map(int, nums))

print(sum(nums_int))