n = int(input())
meet = []
count = 1

for _ in range(n):
    start, end = map(int, input().split())
    meet.append([start, end])

# 회의가 종료 시간을 기준으로 먼저 정렬 후, 끝나는 시간이 같을 경우에는 시작 시간으로 정렬
meet.sort(key=lambda x: (x[1], x[0]))

# 첫 번째 회의의 종료 시간을 대입
end = meet[0][1]

# 두 번째 회의부터 체크
for i in range(1, len(meet)):
    start = meet[i][0] # 다음 회의의 시작 시간

    if start >= end: # 이전에 진행된 회의의 종료 시간보다 다음 회의의 시작 시간이 더 크다면 이용 가능
        count += 1
        end = meet[i][1] # 가능한 회의의 종료 시간을 대입

print(count)