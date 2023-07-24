x, y = map(int, input().split())
one = [1, 2]
two = [2, 1]
three = [2, -1]
four = [1, -2]
count = 0

def dfs(visited, a, b):
    global count

    if not visited[a][b]:
        visited[a][b] = True
        count += 1
        one_x = a + one[0]
        one_y = b + one[1]
        two_x = a + two[0]
        two_y = b + two[1]
        three_x = a + three[0]
        three_y = b + three[1]
        four_x = a + four[0]
        four_y = b + four[1]
        if 0 < one_x <= y and 0 < one_y <= x:
            dfs(visited, a + one[0], b + one[1])
        if 0 < two_x <= y and 0 < two_y <= x:
            dfs(visited, a + two[0], b + two[1])
        if 0 < three_x <= y and 0 < three_y <= x:
            dfs(visited, a + three[0], b + three[1])
        if 0 < four_x <= y and 0 < four_y <= x:
            dfs(visited, a + four[0], b + four[1])

visited = [[False] * (x+1) for _ in range((y+1))]
dfs(visited, 1, 1)
print(count)
