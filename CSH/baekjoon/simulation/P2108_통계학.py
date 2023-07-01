import sys
import collections

N = int(sys.stdin.readline().rstrip())
num = [0] * N

for i in range(N):
    num[i] = int(sys.stdin.readline().rstrip())

num.sort()

# 산술 평균
print(round(sum(num)/N))

# 중앙값
print(num[N//2])

# 최빈값
arr = collections.Counter(num).most_common() # 출력 예시 : [(-2, 1), (1, 1), (2, 1), (3, 1), (8, 1)] -> (a(값), 리스트 안의 a의 개수)
if(len(num) > 1): # 길이가 1 이상인 경우
    if(arr[0][1] == arr[1][1]): # 첫번째와 두번째의 count만 비교해서 같다면 최빈값이 여러 개라는 뜻
        print(arr[1][0]) # 최빈값이 여러 개라면 두번째로 작은 값 출력
    else : # 최빈값이 1개라면
        print(arr[0][0]) # 첫번째 값 출력
else: print(arr[0][0]) # 길이가 1인경우 1개 값(첫번째 값) 출력

# 범위
print(num[-1] - num[0])