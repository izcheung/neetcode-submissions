class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Two pointer going in the same direction
        '''
        You want the buy day to be the lowest price you have seen so far, so if right pointer is less than left AND curr left is lower than what you have seen so far

        [7,1,5,3,6,4]
           l       r
        minLeft = 7
        maxProfit = 5
        l = 0

        '''
        maxProfit = 0
        l = 0
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
                r += 1
            elif prices[r] == prices[l]:
                continue
            else:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
        return maxProfit


