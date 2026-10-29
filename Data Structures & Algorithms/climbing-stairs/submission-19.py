class Solution:
    def climbStairs(self, n: int) -> int:

        memo = {}

        def dfs(n):
            if n in memo:
                return memo[n]
            if n == 0:
                return 1
            if n < 0:
                return 0
            
            oneStep = dfs(n-1)
            twoStep = dfs(n-2)

            res = oneStep + twoStep

            memo[n] = res
            return res
            
        return dfs(n)