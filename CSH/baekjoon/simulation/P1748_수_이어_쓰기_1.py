import sys

n = input()

comp = len(n) - 1

answer = 0

for i in range(comp):
    answer += 9 * (10 ** i) * (i + 1)
answer += ((int(n) - (10 ** comp)) + 1) * (comp + 1)

print(answer)


# 처음풀이 (시간 초과)
# N = int(sys.stdin.readline().rstrip())
# result = ''
#
# for i in range(1, N+1):
#     result += str(i)
#
# print(len(result))