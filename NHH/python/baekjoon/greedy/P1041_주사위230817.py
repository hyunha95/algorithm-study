import sys

N = int(input())

dices =list(map(int, input().split()))
dices.sort(reverse=True)

answer = 0

if N == 1:
    answer += sum(dices) - max(dices)
elif N == 2:
    answer += dices[3] * (2 ** N)
    answer += dices[5] * (N ** 3)
    answer += dices[4] * (N ** 3)
else:
    # answer += dices[3] * (N * N) # 4번째로 큰수
    answer += dices[5] * (N * 4) # 가장 작은 수
    answer += dices[4] * (N * 4) # 가장 작은 수 다음 수

    # 윗 면
    answer += dices[3] * 4 # 모서리
    answer += dices[4] * 4 * (N - 2)
    answer += dices[5] * 1




print(answer)


# 윗면에서 가장 작은 수의 개수
# 3 = 1
# 4 = 4
# 5 = 9
# 6 = 16

# 11111
# 12221
# 12221
# 12221
# 11111

# 윗면
# 323
# 212
# 323

# 4개의 면
# 112
# 112
# 112


