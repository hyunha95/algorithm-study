# 시간 복잡도 때문에 이중 for문 사용하면 시간초과 발생
# 딕셔너리로 풀이 진행

import sys

n = int(sys.stdin.readline().rstrip())
cards = list(map(int, sys.stdin.readline().split()))


m = int(sys.stdin.readline().rstrip())
candidate = list(map(int, sys.stdin.readline().split()))

count = {}
for card in cards:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1
 # count =  {6: 1, 3: 2, 2: 1, 10: 3, -10: 2, 7: 1}

for num in candidate:
    result = count.get(num) # value값을 조회할 때 count[key] 를 사용할 수 있지만 없는 key값에 대해서는 keyError가 발생. get으로 가져오면 없는 key에 대해서 None을 반환
    if result is None:
        print(0, end=" ")
    else:
        print(result, end=" ")