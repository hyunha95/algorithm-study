import sys
from collections import deque

t = int(input())

for _ in range(t):
    size, order = map(int, sys.stdin.readline().rstrip().split())
    important = deque(list(map(int, sys.stdin.readline().rstrip().split())))
    orders = deque(list(range(size)))
    result = 0

    # 중요도가 존재하는 동안 반복문 실행
    while important:
        # 현재 중요도에서 가장 높은 중요도 조회
        maxIm = max(important)

        # 중요도 배열에서 맨 앞에 있는 중요도가 가장 높은 중요도라면
        if important[0] == maxIm:
            important.popleft() # 인쇄
            result += 1 # 인쇄했으니 result에 +1을 해준다.

            # 인덱스 배열에서도 맨 앞 인덱스를 제거해준다. (중요도랑 같은 라이프사이클)
            ip = orders.popleft()
            if ip == order: # 맨 앞 인덱스가 내가 찾는 정수라면
                print(result) # result를 출력하고 반복분을 탈출한다.
                break
        # 맨 앞 중요도가 가장 높은 중요도가 아니라면 로테이션(인덱스 배열과 같이)
        else:
            important.append(important.popleft())
            orders.append(orders.popleft())




