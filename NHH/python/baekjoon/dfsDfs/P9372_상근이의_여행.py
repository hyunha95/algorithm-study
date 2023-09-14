import sys
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited and i != 0:
                queue.append(i)
                visited[i] = True



T = int(input())

for _ in range(T):
    N, M = map(int, input().split()) # countries, planes

    graph = [[0] for _ in range(N+1)]
    visited = [False] * (N+1)
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)

    count = 0
    for i in range(1, N):
        if not visited[i]:
            count += 1
            bfs(graph, i, visited)

    print(count)