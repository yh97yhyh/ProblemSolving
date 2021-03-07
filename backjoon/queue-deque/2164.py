'''
카드2
'''

import sys
from collections import deque

n = int(sys.stdin.readline())

nums = [i+1 for i in range(n)]
queue = deque(nums)

while queue:
    if len(queue) == 1:
        break
    queue.popleft()
    n = queue.popleft()
    queue.append(n)

print(queue[0])