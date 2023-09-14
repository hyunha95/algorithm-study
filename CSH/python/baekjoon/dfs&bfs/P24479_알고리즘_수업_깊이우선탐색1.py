import sys
sys.setrecursionlimit(10**6)

n, m, r = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
count = 0

def dfs(start, graph, visited):
    global count
    count += 1
    visited[start] = count

    for i in graph[start]:
        if  visited[i] == 0:
            dfs(i, graph, visited)

for i in range (m):
    u, v =  map(int, sys.stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, len(graph)):
    graph[i].sort()

dfs(r, graph, visited)

for i in range(1, n + 1):
    print(visited[i])

# 6 4 1
# 2 3
# 1 4
# 1 5
# 4 6