from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(graph, x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1

    return count

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, list(input()))))


answer = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            answer.append(bfs(graph, i, j))

answer.sort()
print(len(answer))
for i in answer:
    print(i)
