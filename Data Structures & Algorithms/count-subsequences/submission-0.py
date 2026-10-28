class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # Subsequences - meaning i can skip letters
        # I need one index for each string
        memo = {}
        def dfs(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            # reached the end meaning matches
            if j == len(t):
                return 1

            if i == len(s):
                return 0
            
            # Match
            total = 0
            if i < len(s) and s[i] == t[j]:
                # Take
                total += dfs(i+1, j+1)
            total += dfs(i+1, j)
            memo[(i,j)] = total
            return total

        return dfs(0,0)

         