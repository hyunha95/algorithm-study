import sys
from collections import deque

def dfs(graph,v, visited):
    visited[v] = True # 노드를 방문 처리 한다.
    print(v, end=' ')
    for i in graph[v]: # 해당 노드에 연결된 노드들을 깊이 우선 탐색을 한다.
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    visited[v] = True
    queue = deque([start]) # 첫 시작 노드를 큐에 넣어준다.

    while queue: # 큐가 빌 때 까지
        num = queue.popleft() # 제일 먼저 삽입된 노드를 뽑는다.
        print(num, end=' ')

        for i in graph[num]: # 해당 노드에 연결된 노드들 중에서
            if not visited[i]:  # 아직 방문하지 않는 노드가 있다면
                visited[i] = True # 다 방문처리하고
                queue.append(i) # 큐에 넣어준다.


n, m, v = map(int, sys.stdin.readline().rstrip().split())

graph = [[] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)

for i in range(m):
    v1, v2 = map(int, sys.stdin.readline().rstrip().split())

    # 양방향으로 정점을 넣어준다.
    graph[v1].append(v2)
    graph[v2].append(v1)
    
# 방문할 노드가 많을 때는 작은 것부터 방문 해야하므로 정렬 처리
for i in range(1, n+1):
    graph[i].sort()

dfs(graph, v, visited)

print() # 줄바꿈

# bfs 실행 전 방문 함수 초기화
visited = [False] * (n+1)
bfs(graph,v, visited)
