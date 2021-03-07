'''
OX 퀴즈
'''

import sys

n = int(sys.stdin.readline())

def getScore(oxs):
    score = 0
    cnt = 0
    for ox in oxs:
        if ox == 'O':
            cnt += 1
            score += cnt
        else:
            cnt = 0
    print(score)

for i in range(n):
    oxs = list(sys.stdin.readline().strip())
    getScore(oxs)