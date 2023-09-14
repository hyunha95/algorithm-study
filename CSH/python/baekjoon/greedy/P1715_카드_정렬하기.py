import sys
import heapq

n = int(sys.stdin.readline())
card = [int(sys.stdin.readline()) for _ in range(n)]
result = 0

if len(card) >= 2:
    heapq.heapify(card) # 리스트를 힙으로 변환
    while len(card) >= 2:
        a = heapq.heappop(card) # 가장 작은 값
        b = heapq.heappop(card) # 그 다음으로 작은 값
        hab = a + b
        heapq.heappush(card, hab)
        result += hab
    print(result)
else:
    print(0)