A, B = map(int, input().split())

count = 1
while A != B:
    if B % 2 == 0:
        B = B // 2
    else:
        if len(str(B)) > 1 and str(B)[-1] == "1":
            B = int(str(B)[:-1])
        else:
            print(-1)
            break

    count += 1

    if A > B:
        print(-1)
        break
else:
    print(count)


