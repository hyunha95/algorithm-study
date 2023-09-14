from collections import deque

T = int(input())
for _ in range(T):
    N = int(input())
    trees = sorted(list(map(int, input().split())))
    trees.reverse()

    queue = deque([trees[0]])
    for i in range(1, N):
        if i % 2 != 0:
            queue.append(trees[i])
        else:
            queue.appendleft(trees[i])

    gap_arr = []
    for i in range(len(queue) - 1):
        gap_arr.append(abs(queue[i] - queue[i+1]))
    gap_arr.append(abs(queue[0] - queue[-1]))

    print(max(gap_arr))