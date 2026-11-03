class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]

            if i == n:
                return 1
            if i > n:
                return 0

            oneStep = dfs(i+1)
            twoStep = dfs(i+2)
            
            res = oneStep + twoStep
            memo[i] = res
            return res

        return dfs(0)