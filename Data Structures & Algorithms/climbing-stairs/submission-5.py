class Solution:
    def climbStairs(self, n: int) -> int:
      '''
      n = 2

      1 + 1
      2

      n = 3

      Constraints:
      - At least one step
      - What is the maximum value of n (recursive vs dp)


      ex:

      n = 3  climbStairs(2) +  climbStairs(1)
        =     2 + 1
      n = 2  climbStairs(1) + climbStairs(0) = 2
          
      Time complexity O(2^n)
      -> O(n)

      '''
      memo = {}

      def dfs(n):
        if n in memo:
          return memo[n]
        if n <= 2: 
          return n
        memo[n] = dfs(n-1) + dfs(n-2)
        return memo[n]
        
      return dfs(n)


