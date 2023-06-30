def solution(n, lost, reserve):

    arr = [0] * n
    for i in lost:
        arr[i - 1] -= 1
    for i in reserve:
        arr[i - 1] += 1

    for i in range(0, n-1):
        if arr[i] * arr[i+1] == -1:
            arr[i] = 0
            arr[i+1] = 0

    return n-(arr.count(-1))

n = 5
lost = [2, 4]
reserve = [1,3,4]
print(solution(n, lost, reserve))