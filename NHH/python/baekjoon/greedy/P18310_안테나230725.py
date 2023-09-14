N = int(input())
locations = sorted(list(map(int, input().split())))

middle = N // 2

if N % 2 == 0:
    print(locations[middle-1])
else:
    print(locations[middle])

