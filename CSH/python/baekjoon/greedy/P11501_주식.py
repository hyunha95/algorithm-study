import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    stoke = list(map(int, sys.stdin.readline().split()))
    sum = 0

    if sorted(stoke) == stoke: # 오름 차순 정렬하는 것과 stoke이 같다면 맨 마지막에 팔아도 된다.
        max_s = max(stoke) # max값 (맨 마지막 값)

        for i in range(n-1):
           sum += max_s - stoke[i] # max 값에서 뺀 값을 누적 합 해준다.

        print(sum)

    elif sorted(stoke, reverse=True) == stoke: # 내림 차순 정렬한 것과 stoke이 다르다면 안사도 됨
        print(0)

    else : # 주가가 올랐다가 내려간다면
        max_s = max(stoke)
        for i in range(n -1):
            if stoke[i] != max_s: # max 값이 아니라면 max값에서 빼준다.
                sum += max_s - stoke[i]
            elif stoke[i] == max_s: # max값이 나왔다면 max값 이후 주가부터 다시 max값을 구해준다. 1 1 3 1 2 일 경우 처음 3일때 주식을 팔고 2일때 팔아야 하므로 max값을 3에서 2로 변경
                max_s = max(stoke[i+1:])
        print(sum)
