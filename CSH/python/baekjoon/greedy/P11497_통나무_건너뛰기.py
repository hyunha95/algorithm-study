t = int(input())

for _ in range(t):
    n = int(input())
    tree = list(map(int, input().split()))
    result = 0

    tree.sort()
    m = tree[-1] # max값

    # m값을 기준으로 왼쪽 배열
    left = [tree[i] for i in range(len(tree)-1) if i % 2 == 0]

    # m값을 기준으로 오른쪽 배열
    right = sorted([tree[i] for i in range(len(tree)-1) if i % 2 != 0], reverse= True)

    # 왼쪽 배열 + m + 오른쪽 배열 합침
    left.append(m)
    arr = left + right

    # 인접한 통나무 중에서 차이가 많이 나는 길이를 구함
    for i in range(n-1):
        if result < abs(arr[i]-arr[i+1]):
            result = abs(arr[i]-arr[i+1])

    print(result)







