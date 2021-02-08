'''
덩치
'''

import sys

n = int(sys.stdin.readline())

peoples = []
for i in range(n):
    people = []
    kg, cm = map(int, sys.stdin.readline().split())
    people.append(kg)
    people.append(cm)
    peoples.append(people)

answer = []
for p1 in peoples:
    count = 1
    for p2 in peoples:
        if p1[0] < p2[0] and p1[1] < p2[1]: # 키와 몸무게가 모두 커야 덩치가 크다
            count += 1
    answer.append(count)

for a in answer:
    print(a, end=' ')