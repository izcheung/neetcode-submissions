class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Graph question
        # iterate through the entire grid, when i encounter a 1 I should explore it completely, (using a set to keep track of visited coordinates), increment the islandCount after it is completely visited
        # Grid - check boundaries, visited, "1"


        visited = set()
        count = 0

        def dfs(r, c, visited):
            # check boundaries
            rowInBounds = 0 <= r < len(grid)
            colInBounds = 0 <= c < len(grid[0])
            if not rowInBounds or not colInBounds:
                return False
            # if already visited
            if (r,c) in visited:
                return False
            if grid[r][c] == "0":
                return False
            
            visited.add((r,c))

            # Visit in 4 directions
            dfs(r+1, c, visited)
            dfs(r-1, c, visited)
            dfs(r, c+1, visited)
            dfs(r, c-1, visited)

            return True
            # Return true once island is completely explored
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if dfs(r,c,visited):
                    count += 1
        return count


