'''
구현
게임 개발
'''

# 세로, 가로 입력 (n * m)
n, m = map(int, input().split())

# 시작위치 (x, y) ,동서남북 입력
x, y, direction = map(int, input().split())

# 방문 위치 저장
visited = [[0] * m for _ in range(n)]

visited[x][y] = 1

# 맵 정보 입력
array = []
for i in range(n):
    array.append(list(map(int, input().split())))
    print(i)
    
# 북, 동, 남, 서 방향으로 이동
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turnLeft():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turnLeft()
    
    # 전진했을 경우
    afterX = x + dx[direction]
    afterY = y + dy[direction]

    if visited[afterX][afterY] == 1 or array[afterX][afterY] == 1: # 바다거나 방문했을 경우
        turn_time += 1
    else: # 갈 수 있을 경우
        x = afterX
        y = afterY
        visited[x][y] = 1
        count += 1
        turn_time = 0
        continue

    if turn_time == 4: # 네 방향이 모두 막혔을 경우
        afterX = x - dx[direction] # 후진했을 경우
        afterY = y - dy[direction]
        if array[afterX][afterY] == 1: # 바다일 경우
            break
        else: # 뒤로 갈 수 있을 경우
            x = afterX
            y = afterY
        turn_time = 0

print(count)
