import sys
from queue import PriorityQueue

N = int(input())

queue = PriorityQueue()
for _ in range(N):
    queue.put(int(sys.stdin.readline().rstrip()))

if queue.qsize() == 1:
    print(0)
else:
    temp = []
    for _ in range(queue.qsize()-1):
        first = queue.get()
        second = queue.get()
        temp.append(first)
        temp.append(second)
        queue.put(first + second)

    print(sum(temp))
