n = int(input())
target1, target2 = map(int, input().split())
m = int(input())

result = 0
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(start, depth):
    global result
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            visited[i] = True
            if i == target2:
                result = depth
            else:
                dfs(i, depth + 1)

dfs(target1, 0)
print(result + 1 if result > 0 else -1)