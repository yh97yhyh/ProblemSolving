'''
< 네트워크 >
'''

n1 = 3
c1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
n2 = 3
c2 = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

def solution(n, computers):
    answer = 0
    bfsList = []

    for computer in range(n): # 전체 컴퓨터 네트워크 검사
        if computer in sum(bfsList, []): # bfsList에 있는 노드이면 네트워크 검사 X
            continue

        visited = []
        queue = [computer] # 시작 node 컴퓨터

        while queue: # 현재 컴퓨테에서 bfs 방문 (네트워크 찾기)
            current = queue.pop()
            for neighbor in range(len(computers[current])):
                if current == neighbor:
                    continue
                if (not neighbor in visited) and (computers[current][neighbor] == 1): # 방문하지 않았고, 이웃 노드이면 queue에 추가
                    queue.insert(0, neighbor)
            visited.append(current)
        bfsList.append(visited)

    return len(bfsList)


print('example1 : ', solution(n1, c1))
print('example2 : ', solution(n2, c2))


def bfs(n, computers):
    answer = 0
    visited = []
    queue = [0]

    while queue:
        current = queue.pop()
        for neighbor in range(len(computers[current])):
            if current == neighbor:
                continue
            if (not neighbor in visited) and (computers[current][neighbor] == 1):
                queue.insert(0, neighbor)
        visited.append(current)

    return visited

