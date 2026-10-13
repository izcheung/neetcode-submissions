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

        distance = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                char = grid[r][c]
                if char != 0:
                    grid[r][c] = distance
                if 0 <= r + 1 < len(grid) and grid[r+1][c] == 2147483647 and (r+1, c) not in seen:
                    q.append((r+1,c))
                    seen.add((r+1,c))
                if 0 <= r - 1 < len(grid) and grid[r-1][c] == 2147483647 and (r-1, c) not in seen:
                    q.append((r-1,c))
                    seen.add((r-1,c))
                if 0 <= c + 1 < len(grid[0]) and grid[r][c+1] == 2147483647 and (r, c+1) not in seen:
                    q.append((r,c+1))
                    seen.add((r, c+1))
                if 0 <= c - 1< len(grid[0]) and grid[r][c-1] == 2147483647 and (r, c-1) not in seen:
                    q.append((r,c-1))
                    seen.add((r, c-1))
            distance += 1


