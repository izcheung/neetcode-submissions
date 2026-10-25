class Solution:
    def rob(self, nums: List[int]) -> int:

        def dfs(i, houses, memo):
            if i in memo:
                return memo[i]
            if i >= len(houses):
                return 0
            doRob = houses[i] + dfs(i+2, houses, memo)
            dontRob = dfs(i+1, houses, memo)
            memo[i] = max(doRob, dontRob)
            return memo[i]


        def helper():
            memo1 = {}
            memo2 = {}
            robFirst = dfs(0, nums[1:], memo1)
            robSecond = dfs(0, nums[:-1], memo2)
            return max(robFirst, robSecond)

        if len(nums) == 1:
            return nums[0]

        return helper()