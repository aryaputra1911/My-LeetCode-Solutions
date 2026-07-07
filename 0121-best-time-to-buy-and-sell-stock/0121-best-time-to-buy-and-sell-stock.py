class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_value = prices[0]
        max_profit = 0

        for i in prices:
            if i < min_value:
                min_value = i
            else:
                profit = i - min_value
                if profit > max_profit:
                    max_profit = profit
        return max_profit


        