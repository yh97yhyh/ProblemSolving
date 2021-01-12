'''
정렬
두 배열의 원소 교체
'''

n, k = map(int, input().split())

# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

a = [1, 2, 5, 4, 3]
b = [5, 5, 6, 6, 5]

for i in range(k):
    a.sort()
    b.sort(reverse=True)

    if a[0] < b[0]:
        a[0], b[0] = b[0], a[0]

print(sum(a))