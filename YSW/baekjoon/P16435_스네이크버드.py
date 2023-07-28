import sys

N, L = map(int, sys.stdin.readline().split())

h_list = list(map(int, sys.stdin.readline().split()))
h_list.sort()

for i in range(0, N):
    if L >= int(h_list[i]):
        L = L + 1
    else:
        break

print(L)