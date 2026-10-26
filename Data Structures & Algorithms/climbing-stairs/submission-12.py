class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i <= 0:
                return 0
            if i == 1:
                return 1
            if i == 2:
                return 2
            takeStep = dfs(i-1)
            skipStep = dfs(i-2)
            memo[i] = takeStep + skipStep
            return memo[i]
            
        return dfs(n)
            
