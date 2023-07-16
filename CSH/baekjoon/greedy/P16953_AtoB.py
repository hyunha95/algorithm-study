a, b = map(int, input().split())
result = 1
flag = False

while b >= a:

    if b % 2 == 0 :
        b //= 2

    elif str(b)[-1] == "1":
        b = int(str(b)[:-1])

    else:
        break
    result += 1

    if b == a:
        flag = True
        break

if flag :
    print(result)
else :
    print(-1)