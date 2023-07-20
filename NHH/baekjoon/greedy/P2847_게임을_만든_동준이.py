import sys
N = int(input())

arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline().rstrip()))

arr = list(reversed(arr))

answer = 0
max = arr[0]
for i in range(1, len(arr)):
    if arr[i] >= max:
        while arr[i] >= max:
            answer += 1
            arr[i] -= 1

    max = arr[i]
print(answer)

