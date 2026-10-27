class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Sort the nums
        total = sum(nums)
        if total % 2 == 1:
            return False
        half = total / 2

        memo = {}

        def dfs(i, half):
            if (i,half) in memo:
                return memo[(i,half)]
            if i == len(nums):
                return False
            if half == 0:
                return True
            if half < 0:
                return False
            take = dfs(i+1, half - nums[i])
            dontTake = dfs(i+1, half)
            memo[(i,half)] = take or dontTake
            return take or dontTake

        return dfs(0, half)
