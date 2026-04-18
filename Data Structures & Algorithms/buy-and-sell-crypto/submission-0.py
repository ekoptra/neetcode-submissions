class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prices, max_price = [0] * len(prices), 0
    
        for i in range(len(prices) -1, -1, -1):
            max_price = max(max_price, prices[i])
            max_prices[i] = max_price
        
        max_profit = 0
        for i in range(len(prices)):
            max_profit = max(max_profit, max_prices[i] - prices[i], 0)
        
        return max_profit
    