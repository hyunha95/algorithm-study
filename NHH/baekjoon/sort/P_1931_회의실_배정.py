import sys

N = int(input())

arr = []
for _ in range(0, N):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    arr.append([a, b])

arr.sort(key=lambda a: (a[1], a[0]))

answer = 1
current = arr[0][1]
for i in range(0, len(arr) - 1):
    if current <= arr[i + 1][0]:
        answer += 1
        current = arr[i + 1][1]

print(answer)