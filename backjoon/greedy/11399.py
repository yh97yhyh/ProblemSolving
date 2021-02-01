'''
ATM
'''

n = int(input())
line = list(map(int, input().split()))
line.sort()

times = []

count = 0
for p in line:
    count += p
    times.append(count)

print(sum(times))