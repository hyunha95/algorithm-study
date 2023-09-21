import sys
n, m = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))

for _ in range(m):
    card.sort()
    tmp = card[0] + card[1]
    card[0], card[1] = tmp, tmp

print(sum(card))