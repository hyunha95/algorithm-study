import sys
from queue import PriorityQueue

N = int(input())

queue = PriorityQueue()
for _ in range(N):
    S, T = map(int, sys.stdin.readline().rstrip().split())
    queue.put((S, T))

answer = 1
current = queue.get()[1]
while queue.qsize() != 0:
    next = queue.get()[0]
    if current <= next:
        answer += 1

print(answer)
