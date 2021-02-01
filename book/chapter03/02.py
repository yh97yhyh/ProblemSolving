'''
그리디
큰 수의 법칙
'''

N, M, K = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort(reverse=True)
answer = 0

n1 = num_list[0]
n2 = num_list[1]

count = 0
for i in range(M):
    if count < K:
        answer += n1
        count += 1
    else:
        answer += n2
        count = 0
    # print(count, answer)

print(answer)
