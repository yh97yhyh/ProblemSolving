'''
나이순 정렬
'''

import sys

n = int(sys.stdin.readline())

users = []
for i in range(n):
    age, name = sys.stdin.readline().strip().split()
    age = int(age)
    users.append((age, name, i))

users.sort(key = lambda user:(user[0], user[2])) # 나이 순, 가입 순

for age, name, num in users:
    print(age, end=' ')
    print(name)