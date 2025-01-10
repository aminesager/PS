def maxProfit(prices):
    
    profit = 0
    actual = prices[0]    
    
    for i in range(1,len(prices)):
        if actual < prices[i]:
            profit += prices[i] - actual
        actual = prices[i]
            
    return profit


prices = [1,4,9,1]
