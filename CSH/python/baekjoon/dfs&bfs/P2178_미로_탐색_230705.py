# 이코테 설명 들은 후 다음날 문풀. 다시 풀어볼 것

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
miro = []

for _ in range(n):
    miro.append(list(map(int, sys.stdin.readline().rstrip())))

# 방향 벡터
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x,y):
    que = deque()
    que.append((x, y))

    # 큐가 빌 때 까지 반복
    while que:
        x, y = que.popleft()

        # 현재 위치에서 상하좌우 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 공간을 벗어난 경우에는 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 이동할 수 없는 곳도 무시
            if miro[nx][ny] == 0:
                continue

            # 이동할 수 있는 경우에 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y] + 1 # 직전 노드 까지의 거리 합에 + 1을 더해줘서 기록한다.
                que.append((nx, ny)) # 해당 노드를 큐에 삽입

    # 가장 오른쪽 아래까지의 최단 거리 반환
    return miro[n-1][m-1] 

print(bfs(0, 0))
