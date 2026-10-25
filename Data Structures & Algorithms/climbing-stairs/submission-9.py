class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dfs(n):
         
            if n in memo:
                return memo[n]
            if n <= 2:
                memo[n] = n
                return n
          
     
            one_step = dfs(n-1)
            two_step = dfs(n-2)
            memo[n] = one_step + two_step
            return memo[n]
        return dfs(n)