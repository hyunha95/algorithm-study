import sys
sys.setrecursionlimit(10000000)

def dfs(graph, start, visited):
    visited[start] = True
    global count
    count += 1
    answer[start] = count

    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)

N, M, start = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
count = 0
answer = [0] * (N+1)
for _ in range(M):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N):
    graph[i].sort()

dfs(graph, start, visited)

for i in range(1, len(answer)):
    print(answer[i])
