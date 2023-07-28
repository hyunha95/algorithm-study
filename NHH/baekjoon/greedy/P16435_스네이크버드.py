N, L = map(int, input().split())
height_of_fruits = sorted(list(map(int, input().split())))

for height_of_fruit in height_of_fruits:
    if L >= height_of_fruit:
        L += 1

print(L)