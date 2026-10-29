class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        seen = set()
        queue = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    seen.add((r,c))
                    queue.append((r,c))
        
        distance = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        while queue:
            lenQ = len(queue)
            for i in range(lenQ):
                r, c = queue.popleft()
                grid[r][c] = distance

                for x,y in directions:
                    newX = r + x
                    newY = c + y

                    rowInBounds = 0 <= newX < len(grid)
                    colInBounds = 0 <= newY < len(grid[0])

                    if rowInBounds and colInBounds and grid[newX][newY] == 2147483647:
                        if (newX, newY) not in seen:
                            queue.append((newX,newY))
                            seen.add((newX, newY))
                    
            distance += 1

