from collections import deque

N = int(input())
M = int(input())

graph = [[False] * (N + 1) for _ in range(N + 1)]
visited = [False] * (N + 1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

def bfs(V):
    queue = deque([V])
    visited[V] = True

    answer = 0
    while queue:
        V = queue.popleft()
        for i in range(1, N + 1):
            if not visited[i] and graph[V][i]:
                visited[i] = True
                queue.append(i)
                answer += 1

    return answer

def dfs(V):
    visited[V] = True

    answer = 0
    for i in range(1, N + 1):
        if not visited[i] and graph[V][i]:
            answer += 1
            dfs(i)


print(bfs(1))