n, m = map(int, input().split())
arr = []
result = 0

for _ in range(m):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: (x[0], x[1])) # 패키지 가격을 기준으로 오름차순 정렬
pack = arr[0][0] # 가장 낮은 패키지 가격

arr.sort(key=lambda x: (x[1], x[0])) # 낱개 가격을 기준으로 오름차순 정렬
one = arr[0][1] # 가장 낮은 낱개 가격


while n > 0:

    # 만약에 패키지 가격이 낱개 가격보다 작다면 낱개 가격을 패키지 가격으로 교체
    if pack < one:
        one = pack

    # 만약에 낱개 * 6의 가격이 패키지 가격보다 작다면 낱개를 6개 구매하는게 더 나으므로 패키지 가격을 낱개 * 6의 가격으로 교체
    elif pack > one * 6 :
        pack = one * 6

    # 필요한 기타줄의 개수가 6개 이상이라면 패키지 가격으로 계산
    if n >= 6:
        result += pack * (n // 6)
        n -= 6 * (n // 6)

    else: # 필요한 기타줄의 개수가 6개 미만이라면

        if pack < (one * n): # 낱개 * 필요한 기타줄의 개수 가격이 패키지 가격보다 크다면 패키지를 구매하는게 나음
            result += pack # 패키지 구매
        else : # 낱개의 가격이 더 저렴하다면
            result += (one * n) # 낱개 구매

        break

print(result) # 결과 출력