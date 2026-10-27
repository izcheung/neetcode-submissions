class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # final destination is m = 2, n = 5
        # starting at 0,0
        # Return number of ways

        # down = m + 1
        # right = n + 1
        memo = {}
        seen = set()
        def dfs(r,c):
            rowInBounds = 0 <= r < m
            colInBounds = 0 <= c < n

            if not rowInBounds or not colInBounds:
                return 0
            if (r,c) in seen:
                return 0
            if r == m-1 and c == n-1:
                return 1
            if (r,c) in memo:
                return memo[(r,c)]

            seen.add((r,c))
            total = 0
            total += dfs(r+1, c)
            total += dfs(r, c+1)
            
            seen.remove((r,c))
            memo[(r,c)] = total
            return total
        return dfs(0,0)
             