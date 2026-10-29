class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # ith balloon cannot be reused
        memo = {}
        def dfs(nums):
            if nums in memo:
                return memo[nums]
            if len(nums) == 0:
                return 0
         
            maxCoin = 0
            for i in range(len(nums)):
                product = nums[i]
                leftInBounds = 0 <= i - 1 < len(nums)
                rightInBounds = 0 <= i + 1 < len(nums)
                if leftInBounds:
                    product *= nums[i - 1]
                if rightInBounds:
                    product *= nums[i + 1]
                newTuple = tuple(nums[:i] + nums[i+1:])
                pop = product + dfs(newTuple)
                maxCoin = max(pop, maxCoin)
            memo[nums] = maxCoin
            return maxCoin
        start = tuple(nums)
        return dfs(start)

          