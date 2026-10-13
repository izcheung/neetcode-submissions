class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Return the max size
        maxi = 0
        # Grid question - seen, 4 directions, water, explore
        seen = set()

        def findSize(r,c):
            # Out of bounds?
            rowInBounds = 0 <= r < len(grid)
            colInBounds = 0 <= c < len(grid[0])
            if not rowInBounds or not colInBounds:
                return 0

            # Seen? 
            if (r,c) in seen:
                return 0

            # Water?
            if grid[r][c] == 0:
                return 0
                
            seen.add((r,c))
            
            size = 1
            size += findSize(r+1,c)
            size += findSize(r-1,c)
            size += findSize(r,c+1)
            size += findSize(r,c-1)
            return size


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    size = findSize(r, c) # returns the islands size
                    maxi = max(size, maxi)
        return maxi