import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
img = []
total = 0
count = 0
result = []

for i in range(n):
    img.append(list(map(int, sys.stdin.readline().split())))

def dfs(x, y):
    global count

    # 범위 체크
    if x < 0 or y < 0 or x >= n or y >= m:
        return False

    if img[x][y] == 1:
        img[x][y] = 0
        count += 1 # 1이면 그림의 넓이를 1씩 더해줘서 구한다.

        # 상하좌우 체크
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

for i in range(n):
    for j in range(m):
        if dfs(i,j):
            total += 1 # 총 그림이 몇 개인지 체크
            result.append(count) # 각 그림의 넓이를 넣어주고
            count = 0 # 초기화 한다.

if total == 0: # 그림의 개수가 0개라면 0을 출력
    print(0)
    print(0)
else :
    print(total)
    print(max(result))