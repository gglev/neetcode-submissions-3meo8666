class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_sum = 0
        current_sum = prices[0]
        for i in range(1,len(prices)):
            profit = prices[i] - current_sum
            if profit > max_sum:
                max_sum = profit
            if prices[i] < current_sum:
                current_sum = prices[i]
        return max_sum