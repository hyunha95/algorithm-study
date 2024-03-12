from collections import deque

def bfs(start, limit, graph, visited, depth, arr):
    queue = deque([start])
    visited[start] = True

    if depth == limit:
        return

    while queue:
        start = queue.popleft()
        for i in range(1, 101):
            if not visited[i] and not graph:
                if depth == 1:
                    arr.append(5)
                    bfs(i, limit, graph, visited, depth + 1, arr)
                else:
                    arr.append(10)
                    bfs(i, limit, graph, visited, depth + 1, arr)


def dfs(start, limit, graph, visited, depth, arr):
    visited[start] = True

    if depth == limit:
        return

    for i in graph[start]:
        if not visited[i]:
            if depth == 1:
                arr.append(5)
                dfs(i, limit, graph, visited, depth + 1, arr)
            else:
                arr.append(10)
                dfs(i, limit, graph, visited, depth + 1, arr)


def solution(relationships, target, limit):
    graph = [[] for _ in range(101)]
    visited = [False] * 101

    for relationship in relationships:
        a = relationship[0]
        b = relationship[1]

        graph[a].append(b)
        graph[b].append(a)



    arr = []
    bfs(target, limit, graph, visited, 1, arr)
    answer = sum(arr)
    print(answer)




print(solution([[1,2], [2,3], [2,6], [3,4], [4,5]], 2, 3))