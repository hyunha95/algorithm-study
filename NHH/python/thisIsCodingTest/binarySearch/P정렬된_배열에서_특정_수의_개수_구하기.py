from bisect import bisect_left, bisect_right

def count_by_range(arr, target):

    left_index = bisect_left(arr, target)
    right_index = bisect_right(arr, target)

    result = right_index - left_index
    return result if result > 0 else -1

N, x = map(int, input().split())
arr = list(map(int, input().split()))

print(count_by_range(arr, x))

# 7 2
# 1 1 2 2 2 2 3