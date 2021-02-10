'''
통계학
'''

import sys

n = int(sys.stdin.readline())

nums = []
for i in range(n):
    nums.append(int(sys.stdin.readline()))
nums.sort()

length = len(nums)

# 산술평균
avg = round(sum(nums)/length)
print(avg)

# 중앙값
middle = nums[length//2]
print(middle)

# 최빈값
from collections import Counter
def modefinder(nums):
    c = Counter(nums)
    order = c.most_common()
    maximum = order[0][1]
    modes = []
    for num in order:
        if num[1] == maximum:
            modes.append(num[0])
    return modes
manys = modefinder(nums)
manys.sort()
if len(manys) > 1:
    print(manys[1])
else:
    print(manys[0])

# 범위
sub = max(nums) - min(nums)
print(sub)
