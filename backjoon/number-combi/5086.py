'''
배수와 약수
'''

import sys

numsArr = []
while True:
    nums = list(map(int, sys.stdin.readline().split()))
    if nums == [0, 0]:
        break
    else:
        numsArr.append(nums)

for nums in numsArr:
    if nums[0] % nums[1] == 0: # nums[0]이 배수
        print('multiple')
    elif nums[1] % nums[0] == 0: # nums[0]이 약수
        print('factor')
    else:
        print('neither')