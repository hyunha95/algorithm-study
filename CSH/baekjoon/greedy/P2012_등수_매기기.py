import sys

n = int(sys.stdin.readline())
rank = [int(sys.stdin.readline()) for _ in range(n)]
result = 0

rank.sort()

for i in range(1, n+1):
    result += abs(i - rank[i-1])
print(result)


