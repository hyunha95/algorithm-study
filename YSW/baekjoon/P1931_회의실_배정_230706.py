n = int(input())
lst = []

# 2차원 배열로 입력받은 값을 세팅한다.
for i in range(0, n):
    lst.append(list(map(int, list(input().split()))))

# 회의실 끝나는 시간을 기준으로 정렬한다.
lst.sort(key=lambda x : (x[1], x[0]))

# 정렬해서 가장 먼저 끝나는 회의를 선택해준다.
# 먼저 하나 선택해줬기 때문에 회의실을 배정하는 변수 count에 1을 대입해준다.
end = lst[0][1]
count = 1

for i in range(1, len(lst)):
    # 시작하는 시간을 start로 설정한다.
    start = lst[i][0]

    # end와 시간이 같거나 이후에 회의가 시작된다면, 회의실 배정이 가능하다.
    # 따라서 end 변수를 배정해준 회의실이 마무리되는 시간을 변경해주고 회의실 배정 변수에 1을 추가해준다.
    if start >= end:
        end = lst[i][1]
        count += 1

print(count)