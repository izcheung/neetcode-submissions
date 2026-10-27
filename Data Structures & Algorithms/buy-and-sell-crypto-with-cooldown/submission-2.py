class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i, buying):
            if (i,buying) in memo:
                return memo[(i, buying)]
            if i >= len(prices):
                return 0
            
            if buying:
                buy = dfs(i+1, False) - prices[i]
                notBuy = dfs(i+1, True)
                memo[(i, buying)] = max(buy, notBuy)
            else:
                sell = dfs(i+2, True) + prices[i]
                dontSell = dfs(i+1, False) 
                memo[(i, buying)]= max(sell, dontSell)
            return memo[(i, buying)]
        

        return dfs(0,True)



