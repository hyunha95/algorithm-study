import sys
n = int(sys.stdin.readline().rstrip())
score = [ int(sys.stdin.readline().rstrip()) for _ in range(n)]
result = 0

dasom = score[0]

while True:
    flag = False
    for i in range(1, n):
        if score[i] >= dasom:
            dasom += 1
            score[i] -= 1
            result += 1
            flag = True
    if not flag:
        break

print(result)
