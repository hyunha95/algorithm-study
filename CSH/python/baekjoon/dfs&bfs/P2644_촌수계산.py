import sys
n = int(sys.stdin.readline().rstrip())
p1, p2 = map(int, sys.stdin.readline().rstrip().split())
m = int(sys.stdin.readline().rstrip())

family = [[] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)
result = 0
flag = False

for _ in range(m):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    family[x].append(y)
    family[y].append(x)

def dfs(start , depth):
    global result
    global flag
    if start == p2 : # start가 내가 찾는 사람과 같다면
        result = depth # 이때의 촌수를 result에 담는다.
        flag = True # 촌수가 연결 됐다는 표시
        return
    visited[start] = True
    for i in family[start]:
        if not visited[i]:
            visited[i] = True
            dfs(i, depth + 1) # 촌수를 1씩 늘려가며 찾는다.

dfs(p1, 0)
if flag : # 촌수가 연결됐다면 depth를 출력
    print(result)
else: # 촌수가 연결되지 않았다면 -1 출력
    print(-1)
