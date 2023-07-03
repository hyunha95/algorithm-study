T = int(input())

for i in range(0, T):
    data = input()

    arr = []
    for char in data:
        arr.append(char)

        if char == ")":
            if "(" not in arr:
                break
            arr.pop()
            arr.remove("(")

    print("YES" if len(arr) == 0 else "NO")
    arr.clear()