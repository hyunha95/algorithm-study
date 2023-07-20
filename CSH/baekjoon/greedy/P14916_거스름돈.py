n = int(input())
result = 0

money = [5, 2]

while n > 0:

    if n % 5 ==0:
        result += n//5
        n %= 5
    else:
        n -= 2
        result += 1

    if n == 0:
        print(result)
        break
else:
    print(-1)
