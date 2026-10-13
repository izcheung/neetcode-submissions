from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Nearest treasure - BFS
        # Modify in place
        # Grid question - start from the treasure
        # Modify the number if it is not water
        # I if there is overlap, between bfs, then take the smaller number
 
        seen = set()
        q = deque([])
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append((r,c))
                    seen.add((r,c))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        distance = 1
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                char = grid[r][c]

                for rowI, colI in directions:
                    newR, newC = r + rowI, c + colI
                    if (0 <= newR < len(grid) and 
                    0 <= newC < len(grid[0]) and 
                    grid[newR][newC] == 2147483647 and 
                    (newR,newC) not in seen):
                        grid[newR][newC] = distance
                        q.append((newR, newC))
                        seen.add((newR, newC))
            distance += 1



