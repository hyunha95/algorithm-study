n, l = map(int, input().split())
fruit = list(map(int, input().split()))
fruit.sort()

for i in fruit:
    if l >= i:
        l += 1

print(l)