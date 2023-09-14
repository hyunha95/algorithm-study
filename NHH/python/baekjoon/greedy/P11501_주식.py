T = int(input())

for _ in range(T):
    N = int(input())
    stock_prices = list(map(int, input().split()))
    stock_prices.reverse()

    result = 0
    max_value = stock_prices[0]
    for i in range(1, len(stock_prices)):
        if max_value > stock_prices[i]:
            result += max_value - stock_prices[i]
        elif max_value < stock_prices[i]:
            max_value = stock_prices[i]

    print(result)
