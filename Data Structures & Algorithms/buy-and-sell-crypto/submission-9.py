class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # I want the highest sell price and lowest buy price
        # I cannot sort the array because index represents the day
        # I definitely want the left pointer on the lower number
        # update the left pointer to the right pointer when right pointer is less than left pointer
        left = 0
        maxEarning = 0
        for right in range(0, len(prices)):
            if prices[left] > prices[right]:
                left = right
            else:
                maxEarning = max(maxEarning, prices[right]-prices[left])

        return maxEarning
