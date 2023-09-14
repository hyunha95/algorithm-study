import sys
sys.setrecursionlimit(10**6)

def dfs(x,y):

    if x < 0 or x>=h or y < 0 or y >= w:
        return False

    if island[x][y] == 1:
        island[x][y] = 0

        # 상하좌우
        dfs(x, y - 1)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x + 1, y)

        # 대각선
        dfs(x - 1, y - 1)
        dfs(x - 1, y + 1)
        dfs(x + 1, y + 1)
        dfs(x + 1, y - 1)
        return True

    return False

while True:
    w, h = map(int, sys.stdin.readline().split())
    island = []
    cnt = 0

    if w == 0 and h == 0:
        break

    for _ in range(h):
        island.append(list(map(int, sys.stdin.readline().split())))

    for i in range(h):
        for j in range(w):
            if dfs(i,j):
                cnt += 1

    print(cnt)





