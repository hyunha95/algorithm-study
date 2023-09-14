n, m = map(int, input().split())
cards = sorted(list(map(int, input().split())))

for _ in range(m):
    result = cards[0] + cards[1]
    cards[0] = cards[1] = result
    cards.sort()

print(sum(cards))