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

        # Top row for pacific
        for i in range(len(heights[0])):
            pacific.add((0,i))
            dfs(0, i, pacific)
        
        # Col 0 for pacific
        for i in range(len(heights)):
            pacific.add((i,0))
            dfs(i, 0, pacific)

        # Bottom row for atlantic
        for i in range(len(heights[0])):
            atlantic.add((len(heights)-1,i))
            dfs(len(heights)-1,i, atlantic)

        for i in range(len(heights)):
            atlantic.add((i,len(heights[0])-1))
            dfs(i, len(heights[0])-1, atlantic)

        

        ans = []
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if (r,c) in pacific and (r,c) in atlantic:
                    ans.append([r,c])
        return ans



     




