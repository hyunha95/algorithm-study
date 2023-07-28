import sys

N = int(sys.stdin.readline())

candidate_lst = []

for i in range(0, N):
    if i == 0:
        dasom = int(sys.stdin.readline())
    else:
        candidate_lst.append(int(sys.stdin.readline()))

if N == 1:
    print(0)
elif dasom > max(candidate_lst):
    print(0)
elif dasom == max(candidate_lst):
    print(1)
else:
    count = 0
    while dasom <= max(candidate_lst):
        idx = candidate_lst.index(max(candidate_lst))
        dasom = dasom + 1
        candidate_lst[idx] = candidate_lst[idx] - 1
        count = count + 1
    print(count)