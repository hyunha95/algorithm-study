import sys

N = int(input())
lst = []

# Initialize list
for i in range(0, N):
    people = list(map(int, sys.stdin.readline().split()))
    lst.append(people)

# 다른 사람과 비교했을 때 키와 몸무게가 모두 작은 경우 순위가 밀리는 경우로 등수에 +1을 해줌
for people in lst:
    rank = 1
    for idx in range(0, N):
        if people[0] < lst[idx][0] and people[1] < lst[idx][1]:
            rank += 1
    print(rank)