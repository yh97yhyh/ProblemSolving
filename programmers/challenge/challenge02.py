'''
정수 n이 매개변수로 주어집니다.
다음 그림과 같이 밑변의 길이와 높이가 n인 삼각형에서 맨 위 꼭짓점부터 반시계 방향으로 달팽이 채우기를 진행한 후,
첫 행부터 마지막 행까지 모두 순서대로 합친 새로운 배열을 return 하도록 solution 함수를 완성해주세요.
'''

# def solution(n):
#     answer = []
#     for i in range(1, n+1):
#         result = []
#         for j in range(1, i):
#             if i == n: # 마지막 줄
#                 result.append(i + j - 1)
#             else:
#                 if j == 1:
#                     result.append(i)
#                 else:
#
#     return answer

def solution(n):
    answer = []

    length = int(n * (n+1)/2)

    tmp = [[] for _ in range(n)]

    idx = 0
    while True:
        if idx >= n:
            break
        tmp[idx].append(idx+1)
        idx += 1

    for i in range(n):
        for j in range(i):
            tmp[i].append(0)


    x = 0
    y = -1
    dir = [[0, 1], [1, 0], [-1, -1]]
    d = 0
    limit = n
    cnt = 0
    for i in range(1, length + 1):
        if cnt >= limit:
            cnt = 0
            limit -= 1
            d = (d+1) % 3

        x += dir[d][0]
        y += dir[d][1]
        tmp[y][x] = i
        cnt += 1


    for i in range(len(tmp)):
        for j in range(len(tmp[i])):
            answer.append(tmp[i][j])

    return answer

print(solution(4))
print(solution(5))
print(solution(6))