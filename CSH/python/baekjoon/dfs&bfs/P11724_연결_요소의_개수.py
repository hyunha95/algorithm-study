import sys
sys.setrecursionlimit(10**6) # 이 함수를 사용하면, Python이 정한 최대 재귀 깊이를 변경할 수 있다.

n, m = map(int, sys.stdin.readline().rstrip().split())
visited = [False] * (n+1)

graph = [[] * (m+1) for _ in range(n+1)]
count = 0

for _ in range(m):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(start):
    # 해당 노드를 방문 처리 한다.
    visited[start] = True
    global count

    # 해당 노드의 깊이에 해당하는 노드들을 반복문을 돌며 방문처리한다.
    for i in graph[start]:
        if not visited[i]:
            visited[i] = True
            dfs(i)

# 노드가 1번부터 시작하므로 인덱스 맞춰 주기 위해 1번부터 시작
for i in range(1,n+1):
    # 이미 한번 돌 때 깊이에 있는 노드들을 다 방문하기 때문에 끊긴 경우에만 방문하지 않은 경우가 생김
    if not visited[i]: # 방문하지 않았다면
        dfs(i) # dfs를 수행한다.
        count +=1

print(count)



