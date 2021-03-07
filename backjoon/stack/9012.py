'''
괄호
'''

import sys
from collections import deque

n = int(sys.stdin.readline())

def checkVps(vps):
    stack = deque()
    for i in vps:
        if i == "(":
            stack.append(i)
        else: # "("를 입력 받았을 때, 전에 "("가 없다면 NO VPS
            if not stack:
                print("NO")
                return
            else: # stack에 "("가 있으므로 꺼낸다.
                stack.pop()
    if not stack: # 전부 다 돌았는데 stack에 무언가 남았다면 NO VPS
        print("YES")
        return
    else:
        print("NO")
        return

for i in range(n):
    vps = sys.stdin.readline().strip()
    checkVps(vps)
