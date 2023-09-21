# 아이디어 참고
# 중복되는 영역을 하나로 보는게 핵심
# 범위에 포함되는 영역을 1로 해주고 합을 구하면 된다. (배열엔 0아니면 1이므로 합을 구해주면 됨)
import sys

# 2차원 배열
array = [[0 for j in range(101)] for i in range(101)]
n = int(sys.stdin.readline().rstrip())
answer = 0

for i in range(n):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    for j in range(a, a+10):
        for k in range(b,b+10):
            array[j][k] = 1

for i in array:
    answer += sum(i)

print(answer)


