n = int(input())
k = int(input())
sens = list(map(int, input().split()))
sens.sort() # 일직선이므로 정렬

diff = []

if n <= k: # 집중국의 개수가 센서의 개수보다 많을 경우 각 센서는 하나의 집중국을 점령할 수 있다. 그러므로 영역별 차이는 없음
    print(0)
else :
    for i in range(n-1):
        diff.append(abs(sens[i] - sens[i + 1]))

    diff.sort()

    for _ in range(k-1): # 차이가 많이나는 구간을 자르면 된다. 집중국이 5개면 4번을 자르면 5구간으로 나뉜다.
        diff.pop()

    print(sum(diff))