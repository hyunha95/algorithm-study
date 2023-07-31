N, K = map(int, input().split())
heights = list(map(int, input().split()))

diff = []
for i in range(len(heights)-1):
    diff.append(heights[i+1] - heights[i])

diff.sort()

for _ in range(K-1):
    diff.pop()

print(sum(diff))