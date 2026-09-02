class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def traverse(seen, row, col):
            rowInBound = 0 <= row < len(grid)
            colInBound = 0 <= col < len(grid[0])
            
            if not rowInBound or not colInBound:
                return False
            if (row, col) in seen:
                return False
            if grid[row][col] == "0":
                return False
       

            seen.add((row,col))

            up = traverse(seen, row-1, col)
            down = traverse(seen, row+1, col)
            left = traverse(seen, row, col-1)
            right = traverse(seen, row, col+1)

            return True

        seen = set()
        numIsland = 0
        # iterate through the whole graph
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if traverse(seen, row, col):
                    numIsland += 1
        return numIsland


      
            
        
        