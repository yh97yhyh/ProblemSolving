'''
제로
'''

import sys
from collections import deque

num = int(sys.stdin.readline())
stack = deque()

for i in range(num):
    n = int(sys.stdin.readline())
    if n != 0:
        stack.append(n)
    else:
        stack.pop()

stack = list(stack)
print(sum(stack))

