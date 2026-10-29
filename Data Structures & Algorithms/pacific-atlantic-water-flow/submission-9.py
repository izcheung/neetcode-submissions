class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
               
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(r, c, ocean):
                  
            for row, col in directions:
                newRow = row + r
                newCol = col + c
                
                rowInBounds = 0 <= newRow < len(heights)
                colInBounds = 0 <= newCol < len(heights[0])

                if rowInBounds and colInBounds and heights[newRow][newCol] >= heights[r][c]:
                    if (newRow, newCol) not in ocean:
                        ocean.add((newRow,newCol))
                        dfs(newRow, newCol, ocean)
                
    
        pacific = set()
        atlantic = set()

        ROWS = len(heights)
        COLS = len(heights[0])

        # Top row for pacific and Bottom row for atlantic
        for i in range(COLS):
            pacific.add((0,i))
            dfs(0, i, pacific)
            
            atlantic.add((ROWS-1,i))
            dfs(ROWS-1, i, atlantic)
        
        # Left col for pacific and Right col for atlantic
        for i in range(ROWS):
            pacific.add((i,0))
            dfs(i, 0, pacific)

            atlantic.add((i, COLS-1))
            dfs(i, COLS-1, atlantic)


        ans = []
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if (r,c) in pacific and (r,c) in atlantic:
                    ans.append([r,c])
        return ans



     




