import sys

N,K = map(int, sys.stdin.readline().rstrip().split())
idx=0
number = [0] * N
answer = []

for i in range(N):
    number[i] = i+1

for i in range(N):
    idx += K - 1
    if(idx >= len(number)) :
        idx %= len(number)
    answer.append(str(number.pop(idx)))
print("<",', '.join(answer),">", sep="")




