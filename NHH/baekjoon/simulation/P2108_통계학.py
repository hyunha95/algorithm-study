import sys

N = int(sys.stdin.readline().rstrip())

arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline().rstrip()))

arr.sort()

# 산술평균
print(round(sum(arr)/N))

# 중앙값
new_arr = sorted(arr)
print(new_arr[N//2])

# 최빈값
dic = dict() # 빈도수를 저장하는 dict
for i in arr:
    if i in dic.keys():
        dic[i] += 1
    else:
        dic[i] = 1

max = max(dic.values()) # 최빈값 구하기

most_common_numbers = []
for key in dic:
    if dic[key] == max:
        most_common_numbers.append(key)

if len(most_common_numbers) > 1:
    print(most_common_numbers[1])
else:
    print(most_common_numbers[0])

# 범위
print(new_arr[-1] - new_arr[0])


