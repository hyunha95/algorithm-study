import sys
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                arr[i] = v


N = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N):
    graph[i].sort()

arr = [0] * (N+1)
bfs(graph, 1, visited)

for i in range(2, N+1):
    print(arr[i])