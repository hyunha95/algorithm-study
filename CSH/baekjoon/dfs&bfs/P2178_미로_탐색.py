import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(n):
    graph.append(list((map(int, sys.stdin.readline().rstrip()))))


def bfs(x, y):
    que = deque()
    que.append((x, y))

    while que:
        x, y = que.popleft()

        # 상하좌우로 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 공간을 벗어난 경우
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 0인 경우 이동할 수 없음
            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                que.append((nx, ny))

    return graph[n - 1][m - 1]


print(bfs(0, 0))
