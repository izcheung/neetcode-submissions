class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}
        def dfs(r,c, prev):
            if (r,c,prev) in memo:
                return memo[(r,c,prev)]
            rowInBounds = 0 <= r < len(matrix)
            colInBounds = 0 <= c < len(matrix[0])

            if not rowInBounds or not colInBounds:
                return 0

            if matrix[r][c] <= prev:
                return 0

            length = 1
            first = dfs(r+1, c, matrix[r][c])
            second = dfs(r-1, c, matrix[r][c])
            third = dfs(r, c+1, matrix[r][c])
            fourth = dfs(r, c-1, matrix[r][c])

            res = length + max(first,second,third,fourth)
            memo[(r,c,prev)] = res
            return res

        
        totalLength = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                total = dfs(r,c,-1)
                totalLength = max(total, totalLength)
        return totalLength



