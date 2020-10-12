'''

github.com/minsuk-heo/problemsolving/blob/master/graph/
vertexList
edgeList
adjacencyList

< BFS 너비우선탐색 >
currentNode, Queue, visitedNode
최근접경로

< DFS 깊이우선탐색 >
currentNode, Stack, visitedNode
게임(체스...), cycle이 있는지?

'''


# BFS
__author__ = 'Minsuk Heo'

vertexList = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
edgeList = [(0, 1), (1, 2), (1, 3), (3, 4), (4, 5), (1, 6)]
graphs = (vertexList, edgeList)

print(graphs)

def bfs(graph, start):
    vertexList, edgeList = graph
    visitedList = []
    queue = [start]
    adjacencyList = [[] for vertex in vertexList]

    # fill adjacencyList from graph
    for edge in edgeList:
        adjacencyList[edge[0]].append(edge[1])

    # bfs
    while queue:
        current = queue.pop()
        for neighbor in adjacencyList[current]:
            if not neighbor in visitedList:
                queue.insert(0, neighbor)
        visitedList.append(current)
    return visitedList


# print(bfs(graphs, 0))


# DFS
__author__ = 'Minsuk Heo'

vertexList = ['0', '1', '2', '3', '4', '5', '6']
edgeList = [(0,1), (0,2), (1,0) , (1,3) , (2,0) , (2,4) , (2,5) , (3,1), (4,2) , (4,6), (5,2), (6,4)]
graphs = (vertexList, edgeList)

def dfs(graph, start):
    vertexList, edgeList = graph
    visitedVertex = []
    stack = [start]
    adjacencyList = [[] for vertex in vertexList]

    for edge in edgeList:
        adjacencyList[edge[0]].append(edge[1])

    while stack:
        current = stack.pop()
        for neighbor in adjacencyList[current]:
            if not neighbor in visitedVertex:
                stack.append(neighbor)
        visitedVertex.append(current)
    return visitedVertex

# print(dfs(graphs, 0))
