N = int(input())

answer = [0] * N
arr = []
for i in range(0, N):
    x, y  = input().split()
    arr.append([int(x), int(y)])

for i in range(0, N):
    rank = 1
    for j in range(0, N):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            rank += 1
    print(rank, end=' ')