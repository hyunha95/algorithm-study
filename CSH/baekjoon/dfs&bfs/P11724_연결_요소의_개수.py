import sys
sys.setrecursionlimit(10**6) # 이 함수를 사용하면, Python이 정한 최대 재귀 갚이를 변경할 수 있다.

n, m = map(int, sys.stdin.readline().rstrip().split())
visited = [False] * (n+1)

graph = [[] * (m+1) for _ in range(n+1)]
count = 0

for _ in range(m):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(start):
    visited[start] = True
    global count

    for i in graph[start]:
        if not visited[i]:
            visited[i] = True
            dfs(i)

for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        count +=1

print(count)



