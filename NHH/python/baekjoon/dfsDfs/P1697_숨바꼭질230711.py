from collections import deque

def bfs(start, end):
    queue = deque()
    queue.append(start)

    while queue:
        start = queue.popleft()
        if start == end:
            print(dist[start])
            break
        for nx in (start - 1, start + 1, start * 2):
            if 0 <= nx and nx <= MAX and not dist[nx]:
                queue.append(nx)
                dist[nx] = dist[start] + 1

N, M = map(int, input().split())
MAX = 100001
dist = [0] * MAX
bfs(N, M)

