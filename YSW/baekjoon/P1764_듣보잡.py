import sys
N, M = map(int, sys.stdin.readline().split())

dict = {}

for _ in range(0, N):
    s = sys.stdin.readline()
    dict[s] = 1

result = []

for _ in range(0, M):
    s = sys.stdin.readline()
    if s in dict:
        result.append(s.rstrip())
result.sort()

print(len(result))
for s in result:
    print(s)