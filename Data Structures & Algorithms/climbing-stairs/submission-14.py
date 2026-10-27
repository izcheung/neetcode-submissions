class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(n):
            if n in memo:
                return memo[n]
            # Base case
            if n <= 0:
                return 0

            # Number of ways 
            if n == 1:
                return 1
            if n == 2:
                return 2
            takeStep = dfs(n-1)
            skipStep = dfs(n-2)
            memo[n] = takeStep + skipStep
            return memo[n]
            
        return dfs(n)
            
