'''
구현
게임 개발
'''

# 세로, 가로 입력
n, m = map(int, input().split())

# 방문 위치 저장
visited = [[0] * m for _ in range(n)]

# (x, y) ,동서남북 입력
x, y, direction = map(int, input().split())

visited[x][y] = 1;

# 맵 정보 입력
array = []
for i in range(n):
    array.append(list(map(int, input().split())))
    
# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]