import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
graph = [[] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)
arr = [0] * (n+1)

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start):
    visited[start] = True

    for node in graph[start]:

        if not visited[node]: # 처음 방문 했을 떄가 부모
            visited[node] = True
            arr[node] = start # 방문이 처음이라면 이떄의 start 노드를 부모로 한다.
            dfs(node)

dfs(1) # 루트가 1이므로 1부터 시작

for i in range(2, n+1):
    print(arr[i])