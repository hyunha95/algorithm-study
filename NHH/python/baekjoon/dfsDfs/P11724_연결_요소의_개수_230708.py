import sys
sys.setrecursionlimit(5000)

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(start):
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            dfs(i)

answer = 0
for i in range(1, (N+1)):
    if not visited[i]:
        answer += 1
        dfs(i)

print(answer)