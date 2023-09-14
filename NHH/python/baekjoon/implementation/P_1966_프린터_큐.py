from collections import deque

T = int(input())

for _ in range(T):
    N, M = map(int, input().split()) # N = 문서의 개수, M = 몇 번째
    priority_arr = deque((map(int, input().split())))
    index_arr = deque([i for i in range(N)])

    max_num = max(priority_arr)

    answer = 1
    while priority_arr:

        current_num = priority_arr.popleft()
        current_index = index_arr.popleft()

        if current_num == max_num and M == current_index:
            print(answer)
            break

        if current_num == max_num and len(priority_arr) > 0:
            max_num = max(priority_arr)
            answer += 1
        else:
            priority_arr.append(current_num)
            index_arr.append(current_index)
