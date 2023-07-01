## pypy3으로 돌리면 성공으로 나온다..
# 하지만 이런 문제는 DP로 풀어야하는 것을 알고 있는데 잘 몰라서 DP로는 못풀었다.
import sys

n,m = map(int, sys.stdin.readline().split())

num = []
for _ in range(n):
    num.append(list(map(int, sys.stdin.readline().split())))

k = int(input())
for _ in range(k):
    i,j,x,y =map(int, sys.stdin.readline().split())
    sum = 0
    for X in range(i-1,x):
        for Y in range(j-1,y):
            sum += num[X][Y]
    print(sum)
