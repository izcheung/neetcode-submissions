class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # cannot sort because the indices have meaning
        if len(prices) <= 1:
            return 0
        j = 1
        i = 0
        maxProfit = 0
        while i < len(prices)-1:
            while j < len(prices) and i < len(prices)-1:
                profit = prices[j] - prices[i]
                maxProfit = max(profit, maxProfit)
                if prices[j] < prices[i]:
                    i = j
                    j = i + 1
                else:
                    j += 1
            i += 1
            j = i + 1
        return maxProfit
