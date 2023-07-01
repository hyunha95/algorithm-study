N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

K = int(input())
for _ in range(0, K):
    i, j, x, y = map(int, input().split())

    sum = 0
    for a in range(i-1, x):
        for b in range(j-1, y):
           sum += lst[a][b]

    print(sum)

