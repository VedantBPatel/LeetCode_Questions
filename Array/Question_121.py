#Best Time to To Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price_so_far =float('inf') # min_price = prices[0]
        max_profit = 0
        for price in prices:
            if price < min_price_so_far:
                min_price_so_far = price
            elif price - min_price_so_far > max_profit:
                max_profit = price - min_price_so_far
        return max_profit