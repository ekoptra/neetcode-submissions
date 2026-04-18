class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min, curr_max = prices[0], prices[0]

        val = 0
        for price in prices:
            if price < curr_min:
                val = max(curr_max - curr_min, val)
                curr_min = curr_max = price
            else:
                curr_max = price
                val = max(curr_max - curr_min, val)
        
        return val
    