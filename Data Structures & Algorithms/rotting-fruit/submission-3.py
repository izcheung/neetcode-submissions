from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

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
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q and freshOranges > 0:
            for i in range(len(q)):
                row, col = q.popleft()

                for horz, vert in directions:
                    newRow = row + horz
                    newCol = col + vert

                    rowInBounds = 0 <= newRow < len(grid)
                    colInBounds = 0 <= newCol < len(grid[0])

                    if rowInBounds and colInBounds and grid[newRow][newCol] == 1:
                        if (newRow, newCol) not in seen:
                            q.append((newRow, newCol))
                            seen.add((newRow, newCol))
                            grid[newRow][newCol] = 2
                            freshOranges -= 1         
            minute += 1
            
        if freshOranges > 0:
            return -1
        else:
            return minute
        

            
            

