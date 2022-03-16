class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        lowestPrice = prices[0]
        highestProfit = 0
        for i in range(1, len(prices)):
            profit = prices[i] - lowestPrice
            if profit > 0 and profit > highestProfit:
                highestProfit = profit
            elif prices[i] < lowestPrice:
                lowestPrice = prices[i]
        return highestProfit
            