'''
체스판 다시 칠하기
'''

import sys

n, m = sys.stdin.readline().split()
m = int(m)
n = int(n)

chess = []
for i in range(n):
    line = sys.stdin.readline()
    line = line.replace('\n', '')
    chess.append(line)

firstW = True # 맨 왼쪽 위 칸이 흰색
for i in range(n):
    for j in range(m):
        if chess[i][j] == 'B':
            firstW = False # 맨 왼쪽 위 칸이 검은색
