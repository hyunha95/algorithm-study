n, m = map(int, input().split())
array = list(map(int, input().split()))
result = 0

start = 0
end = max(array)

while start <= end:
    total = 0
    mid = (start + end) // 2

    for tree in array:
        if tree > mid:
            total += (tree-mid)

    # 자른 나무의 길이가 모자르기 때문에 더 잘라야한다.
    if total < m:
        end = mid -1
    # 자른 나무의 길이가 충분하다면 덜 잘라야한다. -> 절단기의 높이를 높이면 됨
    else:
        result = mid  # 적어도 M 미터이기 때문에 일단 조건은 만족하므로 result에 기록
        start = mid + 1

print(result)