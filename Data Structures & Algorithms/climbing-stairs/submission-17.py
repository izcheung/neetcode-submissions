class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]
            if i == 0:
                return 1
            if i < 0:
                return 0

            onestep = dfs(i - 1)
            twostep = dfs(i - 2)

            memo[i] = onestep + twostep

            return memo[i] 

        return dfs(n)
