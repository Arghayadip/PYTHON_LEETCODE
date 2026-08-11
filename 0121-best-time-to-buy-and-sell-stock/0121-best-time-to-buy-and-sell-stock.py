class Solution(object):
    def maxProfit(self, prices):
        min_price = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - min_price)
            min_price = min(min_price, prices[i])

        return profit