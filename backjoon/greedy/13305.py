'''
주유소
'''

import sys

n = int(sys.stdin.readline())
distances = list(map(int, sys.stdin.readline().strip().split()))
prices = list(map(int, sys.stdin.readline().strip().split()))

minPrice = prices[0]
answer = minPrice*distances[0] # 처음은 무조건 기름 충전
for i in range(1, n):
    if i == n-1: # 마지막 도시에 도착
        break
    if prices[i] < minPrice:
        minPrice = prices[i]
    answer += minPrice * distances[i]

print(answer)
