from collections import deque

N = int(input())
cranes = deque(sorted(list(map(int, input().split())), reverse=True))

M = int(input())
boxes = sorted(list(map(int, input().split())))

if max(cranes) < max(boxes):
    print(-1)
else:

    count = 0
    minutes = 1
    while len(boxes) > 0:
        count += 1
        crane = cranes.popleft()
        cranes.append(crane)

        box = boxes.pop()

        if crane < box:
            while True:
                crane = cranes.popleft()
                cranes.append(crane)
                if crane >= box:
                    minutes += 1
                    break

    print(minutes + (count // N))