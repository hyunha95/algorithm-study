# 메모리 초과...
from collections import deque

n, k = map(int, input().split())
result = 0

def bfs():
    global result

    que = deque()
    que.append((n,0))

    while que:
        x , y = que.popleft()

        if x == k :
            result = y
            break

        nx1 = x -1
        nx2 = x + 1
        nx3 = 2 * x

        que.append((nx1, y+1))
        que.append((nx2, y+1))
        que.append((nx3, y+1))


bfs()
print(result)