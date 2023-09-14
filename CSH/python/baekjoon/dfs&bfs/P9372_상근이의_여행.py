from collections import deque
import sys

t = int(sys.stdin.readline())

def bfs(start, count):
    que = deque([start])
    visited[start] = True

    while que:
        if visited.count(True) == n:
            return count
        num = que.popleft()

        for i in graph[num]:
            if not visited[i]:
                que.append(i)
                count +=1
                visited[i] = True

for _ in range(t):
    n,m = map(int, sys.stdin.readline().rstrip().split())
    visited = [False] * (n+1)

    graph = [[] for _ in range(n+1)]

    for i in range(m):
        a,b = map(int, sys.stdin.readline().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)

    p = bfs(1, 0)
    print(p)

