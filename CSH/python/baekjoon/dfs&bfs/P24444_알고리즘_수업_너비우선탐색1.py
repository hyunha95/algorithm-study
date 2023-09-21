import sys
from collections import deque
n, m, r = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
count = 1

for i in range (m):
    u, v =  map(int, sys.stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, len(graph)):
    graph[i].sort()

def bfs(start, graph, visited):
    global count
    que = deque([r])
    visited[start] = count

    while que:
        num = que.popleft()
        for i in graph[num]:
            if visited[i] == 0:
                que.append(i)
                count += 1
                visited[i] = count

bfs(r, graph, visited)

for i in range(1, n + 1):
    print(visited[i])
