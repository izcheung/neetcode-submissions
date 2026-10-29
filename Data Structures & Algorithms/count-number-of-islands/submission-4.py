class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
  
        seen = set()

        def dfs(r,c):
            rowInBounds = 0 <= r < len(grid)
            colInBounds = 0 <= c < len(grid[0])

            if not rowInBounds or not colInBounds:
                return False
            if (r,c) in seen:
                return False
            if grid[r][c] == "0":
                return False
                
            seen.add((r,c))
  
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
    
            return True

        total = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    if dfs(r,c):
                        total += 1
        return total 
