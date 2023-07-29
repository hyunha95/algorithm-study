import sys
from collections import Counter

N = int(sys.stdin.readline())
lst = []

# Initialize List
for i in range(0, N):
    lst.append(int(sys.stdin.readline()))

# 중앙값을 찾기 위해 리스트 정렬을 해줌
lst.sort()

# 최빈값을 찾기 위해 collections의 Counter를 사용함
# 최빈값이 같은 경우 key를 오름차순으로 정렬해서 뿌려준다.
mode = Counter(lst).most_common()
maximum = mode[0][1]

if len(mode) == 1:
    mode_val = mode[0][0]
elif mode[0][1] == mode[1][1]:
    mode_val = mode[1][0]
else:
    mode_val = mode[0][0]

print(round(sum(lst) / N))
print(lst[int(N / 2)])
print(mode_val)
print(max(lst) - min(lst))