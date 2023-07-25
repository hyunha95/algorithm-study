import sys

N = int(input())
expected_arr = []
for _ in range(N):
    expected_arr.append(int(sys.stdin.readline().rstrip()))

expected_arr.sort()

answer = 0
for i in range(N):
    if expected_arr != i + 1:
        answer += abs(expected_arr[i] - (i + 1))

print(answer)
