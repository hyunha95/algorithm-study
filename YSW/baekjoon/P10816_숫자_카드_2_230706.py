import sys

# 숫자 카드의 개수(N) 입력
N = int(sys.stdin.readline())

# N개의 카드에 적힌 숫자를 입력받는다.
cards = list(map(int, sys.stdin.readline().split()))

card_dict = {}

for card in cards:
    if card not in card_dict:
        card_dict[card] = 1
    else:
        card_dict[card] = card_dict.get(card) + 1

# M을 입력받음
M = int(sys.stdin.readline())

# 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수를 입력받음
cards_count = list(map(int, sys.stdin.readline().split()))

result = ''

for card in cards_count:
    if card not in card_dict:
        result += '0\n'
    else:
        result += str(card_dict.get(card)) + '\n'

print(result)