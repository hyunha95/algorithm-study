N = int(input())
A = set(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

answer = ''
for num in B:
    if num in A:
        answer += '1\n'
    else:
        answer += '0\n'

print(answer)