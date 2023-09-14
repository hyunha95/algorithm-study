N, M = map(int, input().split())

arr = []
for _ in range(M):
    a, b = map(int, input().split())
    arr.append([a, b])

min_packet = min(arr, key=lambda x: x[0])[0]
min_single = min(arr, key=lambda x: x[1])[1]

money = 0
# 패킷으로 사는게 낱개보다 저렴하다면 패킷으로 구매
if min_packet > (min_single * 6):
    money += N * min_single
else:
    money += (N//6) * min_packet

    # 구매한 나머지가 싱글로 사는것보다 패킷이 저렴한 경우
    if min_packet < min_single*(N%6):
        money += min_packet
    else:
        # 나머지는 낱개로 구매
        money += min_single*(N%6)

print(money)
