class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        seen = set()

        def findSize(r,c):
            rowInBounds = 0 <= r < len(grid)
            colInBounds = 0 <= c < len(grid[0])
            
            if not rowInBounds or not colInBounds:
                return 0
            if (r,c) in seen:
                return 0
            if grid[r][c] == 0:
                return 0
                
            seen.add((r,c))
            
            size = 1
            size += findSize(r+1,c)
            size += findSize(r-1,c)
            size += findSize(r,c+1)
            size += findSize(r,c-1)
            return size

        maxi = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    size = findSize(r, c)
                    maxi = max(size, maxi)
        return maxi