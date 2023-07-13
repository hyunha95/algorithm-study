import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    answer = []

    N = int(sys.stdin.readline().rstrip())
    arr = []
    for i in range(N):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        arr.append([a, b])

    arr.sort()
    answer.append(arr.pop(0))
    queue = deque(arr)

    while queue:
        a, b = queue.popleft()

        if answer[len(answer)-1][0] > a or answer[len(answer)-1][1] > b:
            answer.append([a, b])

    print(len(answer))
