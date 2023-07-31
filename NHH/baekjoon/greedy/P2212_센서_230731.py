N = int(input())
K = int(input())
coordinates = sorted(set(map(int, input().split())))

if K > N:
    print(0)
else:
    distances = []
    for i in range(len(coordinates) - 1):
        distances.append(coordinates[i + 1] - coordinates[i])

    distances.sort()

    for _ in range(K-1):
        distances.pop()

    print(sum(distances))

