from collections import deque

n = int(input())
card = deque(list(i for i in range(1, n+1)))

while card:
    print(card.popleft() , end=' ')

    if len(card) == 0:
        break
    card.append(card.popleft())


