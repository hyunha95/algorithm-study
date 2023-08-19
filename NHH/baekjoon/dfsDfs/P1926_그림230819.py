# import sys
# sys.setrecursionlimit(10 ** 6)
#
# def dfs(graph, x, y):
#     global size
#
#     for i in range(4):
#         if x <= -1 or x >= n or y <= -1 or y >= m:
#             return False
#
#         if graph[x][y] == 1:
#             graph[x][y] = 0
#             size += 1
#             dfs(graph, x+1, y)
#             dfs(graph, x-1, y)
#             dfs(graph, x, y+1)
#             dfs(graph, x, y-1)
#             return True
#
#         return False
#
# n, m = map(int, input().split())
#
# graph = []
# for i in range(n):
#     graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
#
# count = 0
# size_arr = []
# for i in range(0, n):
#
#     for j in range(m):
#         size = 0
#         if dfs(graph, i, j):
#             count += 1
#             size_arr.append(size)
#
# print(count)
# print(max(size_arr) if len(size_arr) != 0 else 0)
#



from collections import deque

n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(graph, a, b):
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count

paint = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            paint.append(bfs(graph, i, j))

if len(paint) == 0:
    print(len(paint))
    print(0)
else:
    print(len(paint))
    print(max(paint))