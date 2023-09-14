import sys
computer = int(sys.stdin.readline().rstrip())
pair = int(sys.stdin.readline().rstrip())

graph = [[]*(computer+1) for _ in range(computer+1)]
visited = [False] * (computer+1)
result = 0

for i in range(pair):
    v1, v2 = map(int, sys.stdin.readline().rstrip().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

# graph :  [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]

def dfs(graph, start, visited):
    global result # 함수 밖의 변수를 사용하기 위해 global 키워드 사용
    visited[start] = True # 해당 노드를 방문 처리 한다.

    for i in graph[start]:
        if not visited[i]:
            visited[i] = True
            result += 1 # 방문된 노드들이 있을 때마다 result 에 +1 해준다.
            dfs(graph, i, visited)

# 함수 호출
dfs(graph, 1, visited)
print(result)
