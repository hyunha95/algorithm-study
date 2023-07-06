import sys

n = int(sys.stdin.readline())
num1 = set(map(int, sys.stdin.readline().rstrip().split()))

m = int(sys.stdin.readline())
num2 = list(map(int, sys.stdin.readline().rstrip().split()))

answer = ''

for i in num2:
    if i in num1:
        answer += "1\n"
    else:
        answer += '0\n'

print(answer)


