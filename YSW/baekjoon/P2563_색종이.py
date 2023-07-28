import sys

# 100 * 100 너비의 도화지를 준비하자.
drawing_paper = []

# 초기값은 0으로 세팅해준다.
for i in range(0, 100):
    lst = []
    for j in range(0, 100):
        lst.append(0)
    drawing_paper.append(lst)

# 몇 개의 색종이를 도화지에 붙일지 값을 받는다.
N = int(sys.stdin.readline())

# 총 색종이의 너비를 구할 변수
count = 0

# 색종이의 너비가 10 * 10이므로 색종이의 좌표에 해당하는 값에 1을 넣는다.
for i in range(0, N):
    start, end = list(map(int, sys.stdin.readline().split()))
    for j in range(start, start + 10):
        for k in range(end, end + 10):
            drawing_paper[j - 1][k - 1] = 1

# 총 색종이가 칠해진 곳을 센다.
for i in range(0, 100):
    for j in range(0, 100):
        if drawing_paper[i][j] == 1:
            count += 1

print(count)

