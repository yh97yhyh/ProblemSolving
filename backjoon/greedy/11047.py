'''
동전 0
'''

n, k = map(int, input().split())
coin_types = []

for i in range(n):
    coin_types.append(int(input()))

coin_types.sort(reverse=True) # 단위가 큰 동전부터 계산

count = 0
for coin in coin_types:
    if coin > k:
        continue
    count += k // coin
    k = k % coin

print(count)