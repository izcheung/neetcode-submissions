class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Grid question - need a seen set
        seen = set()

        # Iterate through all possible grid starting positions
        def dfs(r,c) -> bool:
            # Inbounds?
            rowInBounds = 0 <= r < len(grid)
            colInBounds = 0 <= c < len(grid[0])
            if not rowInBounds or not colInBounds:
                return False
            # Visited?
            if (r,c) in seen:
                return False
            # Water?
            if grid[r][c] == "0":
                return False
            # Add to seen
            seen.add((r,c))

            # Visit 4 directions to completely explore the island
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

            return True

        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1": # only start if on land
                # Completely explore the island and mark seen
                    if dfs(r,c):
                        res += 1
        return res
