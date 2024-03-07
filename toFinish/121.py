# à refaire

test = [3, 2, 6, 5, 0, 3]


def maxProfit(prices):
    profit = 0
    buy = prices[0]
    pos_buy = 0
    for i in range(1, len(prices), 1):
        if prices[i] < buy:
            buy = prices[i]
            pos_buy = i
    for j in range(pos_buy, len(prices), 1):
        diff = prices[j] - buy
        if diff > profit:
            profit = diff
    for k in range(len(prices) - pos_buy):
        prices.pop()
    better_profit = 0
    if prices:
        better_profit = maxProfit(prices)
    if (better_profit > profit) and (len(prices) > 1):
        profit = better_profit
        maxProfit(prices)
    return profit


print(maxProfit(test))

'''''
profit = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices), 1):
            diff = prices[j] - prices[i]
            if diff > profit:
                profit = diff
    return profit
'''''
