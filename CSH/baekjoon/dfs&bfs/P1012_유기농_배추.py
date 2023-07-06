# 이코테 음료수 얼려 먹기랑 거의 똑같은 문제

import sys
sys.setrecursionlimit(10**6) # 이 함수를 사용하면, Python이 정한 최대 재귀 깊이를 변경할 수 있다.
T = int(sys.stdin.readline().rstrip())

def dfs(x, y):
    if x <= -1 or x >= M or y <= -1 or y >= N:
        return False

    if graph[x][y] == 1: # 배추가 심어져 있다면
        graph[x][y] = 0 # 0으로 변경

        # 해당 배추 위치에서 상하좌우 깊이 탐색
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)

        return True # 상하좌우 다 탐색하고 나면 True 반환 (최초 방문인 정점에 대해서만 True 처리가 된다.)

    return False # 처음 방문한게 아니거나, 배추가 심어져 있지 않은 곳이라면 False 반환

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().rstrip().split())
    graph = [[0] * (N+1) for _ in range(M+1)]
    result = 0

    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().rstrip().split())
        graph[X][Y] = 1 #  배추 위치를 입력 받는다.


    for i in range(M):
        for j in range(N):
            if dfs(i,j) :
                result += 1

    print(result)

