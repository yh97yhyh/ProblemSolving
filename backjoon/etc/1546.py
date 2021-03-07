'''
평균
'''

import sys

n = int(sys.stdin.readline())

scores = list(map(int, sys.stdin.readline().split()))
maxScore = max(scores)

sumScore = 0
for i in range(n):
    scores[i] = scores[i] / maxScore * 100
    sumScore += scores[i]

print(sumScore/n)
