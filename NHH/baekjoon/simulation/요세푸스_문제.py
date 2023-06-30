N, K = input().split()

arr = [i for i in range(0, int(N) + 1)]

answer_list = []
index = 0
# N 만큼 돌면서
while len(answer_list) != N:

    if arr[index] == 0:
        continue

    if index % 3 == 0:




        # K이 최대 인덱스를 넘으면 0으로 최기화
        if K == (len(arr) - 1):
            K = 1



