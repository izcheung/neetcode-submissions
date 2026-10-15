from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Rotting only goes horizontally / vertically - empty space does not propagate the rot
        # Each level traversal is one minute
        # BFS
        # Traverse through the entire grid, append the coord of the rotten fruit into the queue.
        # At the end, check if there is still gruit = 1, if there is return -1
        directions = [(1,0), (-1,0), (0, 1), (0,-1)]
        q = deque()
        seen = set()
        freshOranges = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r,c))
                    seen.add((r,c))
                if grid[r][c] == 1:
                    freshOranges += 1
               
     
        minute = 0
        while q and freshOranges > 0:
            for i in range(len(q)):
                row, col = q.popleft()

                # append to queue
                for direction in directions:
                    horz, vert = direction
                    newRow = row + horz
                    newCol = col + vert
                    rowInBounds = 0 <= newRow < len(grid)
                    colInBounds = 0 <= newCol < len(grid[0])
                    if rowInBounds and colInBounds and (newRow, newCol) not in seen and grid[newRow][newCol] == 1:
                        q.append((newRow, newCol))
                        seen.add((newRow, newCol))
                        grid[newRow][newCol] = 2
                        freshOranges -= 1
            
            minute += 1
        if freshOranges > 0:
            return -1
        else:
            return minute
        

            
            

