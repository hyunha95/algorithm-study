import sys
n = int(sys.stdin.readline().rstrip())
home = []
estate_cnt = 0
home_cnt = 0
count = []

for _ in range(n):
    home.append(list(map(int, sys.stdin.readline().rstrip())))

def dfs(x,y):
    global home_cnt

    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if home[x][y] == 1:
        # 단지내 집수 카운트
        home_cnt += 1
        home[x][y] = 0

        # 상하좌우
        dfs(x, y - 1)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x + 1, y)
        return True
    return False

for i in range(n):
    for j in range(n):
        if dfs(i, j):
            estate_cnt += 1 # 단지 수
            count.append(home_cnt)
            home_cnt = 0 # 한 단지 계산이 끝났으므로 단지 내 집 수 초기화

# 단지내 집 수를 오름차순 정렬
count.sort()

print(estate_cnt)
for i in count:
    print(i)
