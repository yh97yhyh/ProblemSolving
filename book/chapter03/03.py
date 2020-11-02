'''
그리디
숫자 카드 게임
'''

N, M = map(int, input().split())
answer = []

for i in range(N):
    num_list = list(map(int, input().split()))
    answer.append(min(num_list))

print(max(answer))