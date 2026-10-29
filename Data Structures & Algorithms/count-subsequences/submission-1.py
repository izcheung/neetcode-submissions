class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        memo = {}
        
        def dfs(i,j):
            if (i,j) in memo:
                return memo[(i,j)]

            if j == len(t):
                return 1

            if i == len(s):
                return 0
            
            total = 0
            if i < len(s) and s[i] == t[j]:
                total += dfs(i+1, j+1)
            total += dfs(i+1, j)

            memo[(i,j)] = total
            return total

        return dfs(0,0)

         