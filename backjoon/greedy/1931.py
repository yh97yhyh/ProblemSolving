'''
회의실 배정
'''
import sys

n = int(sys.stdin.readline())

meetings = []
for i in range(n):
    meetings.append(list(map(int, sys.stdin.readline().split())))

# 끝나는 시간 오름차순, 끝나는 시간이 같다면 빨리 시작하는 시간 오름차순
meetings.sort(key=lambda x: [x[1], x[0]])

count = 0
start_time = 0
for meeting in meetings:
    if meeting[0] >= start_time:
        start_time = meeting[1] # 다음 회의가 가능한 start_time
        count += 1

print(count)