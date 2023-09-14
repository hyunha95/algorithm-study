n = int(input())

arr = []
for i in range(n):
    arr.append(input())

arr = set(arr)
arr = sorted(arr, key = lambda x : (len(x), x))

for i in arr:
    print(i)