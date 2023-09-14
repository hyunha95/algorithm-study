n, k = map(int, input().split())
group = list(map(int, input().split()))
diff = []

group.sort() # 최소 차이를 구하기 위해 정렬

for i in range(n-1):
    diff.append(abs(group[i] - group[i+1]))

diff.sort()

for _ in range(k-1):
    diff.pop()

print(sum(diff))

