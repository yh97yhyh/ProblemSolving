'''
< 등굣길 >
계속되는 폭우로 일부 지역이 물에 잠겼습니다.
물에 잠기지 않은 지역을 통해 학교를 가려고 합니다.
집에서 학교까지 가는 길은 m x n 크기의 격자모양으로 나타낼 수 있습니다.
아래 그림은 m = 4, n = 3 인 경우입니다.

가장 왼쪽 위, 즉 집이 있는 곳의 좌표는 (1, 1)로 나타내고
가장 오른쪽 아래, 즉 학교가 있는 곳의 좌표는 (m, n)으로 나타냅니다.

격자의 크기 m, n과 물이 잠긴 지역의 좌표를 담은 2차원 배열 puddles이 매개변수로 주어집니다.
오른쪽과 아래쪽으로만 움직여 집에서 학교까지 갈 수 있는 최단경로의 개수를 1,000,000,007로 나눈 나머지를 return 하도록 solution 함수를 작성해주세요.
'''

m1 = 4
n1 = 3
puddles1 = [[2, 2]]

def solution(m, n, puddles):
    answer = 0
    road = [[0 for i in range(m+1)] for j in range(n+1)]
    road[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            if [j, i] in puddles:
                road[i][j] = 0
            else:
                road[i][j] += (road[i-1][j] + road[i][j-1])
    answer = road[-1][-1] % 1000000007
    return answer

print(solution(m1, n1, puddles1))