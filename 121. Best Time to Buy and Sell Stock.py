def maxProfit(prices):
    
    profit = 0
    actual = prices[0]
    for i in range(1, len(prices)):
        if prices[i] < actual:
            actual = prices[i]
        else:
            profit = max(profit, prices[i] - actual)
    
    return profit