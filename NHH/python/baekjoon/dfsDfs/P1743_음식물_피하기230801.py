dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(graph, x, y):
    global count

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= M or ny < 0 or ny >= N:
            continue

        if graph[x][y] == 1:
            count += 1
            dfs(graph, nx, ny)
            graph[x][y] = 0



N, M, K = map(int, input().split()) # 세로, 가로, 음식물 쓰레기의 개수

graph = [[0] * (M+1) for _ in range(N+1) ]
for _ in range(K):
    r, c = map(int, input().split())
    graph[r][c] = 1 # 음쓰 위치 표시

answer = []
for i in range(1, N+1):
    for j in range(1, M+1):
        if graph[i][j] == 1:
            count = 0
            dfs(graph, i, j)
            answer.append(count)

print(max(answer))
