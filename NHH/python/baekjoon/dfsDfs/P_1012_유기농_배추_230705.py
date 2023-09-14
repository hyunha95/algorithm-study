# 재귀 limit 설정
import sys
sys.setrecursionlimit(10000)

T = int(input())

def dfs(x, y):
    for i in range(0, 4):
        if x <= -1 or x >= N or y <= -1 or y >= M:
            return False
        if graph[x][y] == 1:
            graph[x][y] = 0
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
            return True
    return False

for _ in range(T):
    M, N, K = map(int, input().split())

    graph = [[0] * M for _ in range(N)]
    for i in range(0, K):
        X, Y = map(int, input().split())
        graph[Y][X] = 1


    answer = 0
    for i in range(0, N):
        for j in range(0, M):
            if dfs(i, j):
              answer += 1

    print(answer, end='')