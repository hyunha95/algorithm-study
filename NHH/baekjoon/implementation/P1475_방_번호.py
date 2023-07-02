import math

N = input()
count = 0
arr = [0] * 10
for i in range(0, 10):
    if i == 6 or i == 9:
        count += N.count(str(i))
    else:
        arr[i] = N.count(str(i))

max = max(arr) if max(arr) > math.ceil(count / 2) else math.ceil(count / 2)
print(max)