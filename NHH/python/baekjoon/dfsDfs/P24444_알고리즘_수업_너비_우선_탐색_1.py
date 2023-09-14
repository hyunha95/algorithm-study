import sys
from collections import deque
sys.setrecursionlimit(1000000)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    global count
    count += 1
    answer[start] = count

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i] and i != 0:
                queue.append(i)
                visited[i] = True
                count += 1
                answer[i] = count


N, M, R = map(int, input().split())

graph = [[0] for _ in range(N+1)]
visited = [False] * (N+1)
count = 0
answer = [0] * (N+1)
for _ in range(M):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(N+1):
    graph[i].sort()

bfs(graph, R, visited)
print("\n".join(list(map(str,answer[1:]))))
