class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i >= len(nums):
                memo[i] = 0
                return 0
            dontRob = dfs(i+1)
            doRob = nums[i] + dfs(i+2)
            memo[i] = max(dontRob, doRob)
            return memo[i]
        return dfs(0)
    