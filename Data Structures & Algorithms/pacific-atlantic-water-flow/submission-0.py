class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        pac = set()
        atl = set()

        def dfs(r, c, visit, prevHeight):

            rowInBounds = 0 <= r < ROWS
            colInBounds = 0 <= c < COLS

            if ((r,c) in visit):
                return
            if not rowInBounds or not colInBounds:
                return
            if heights[r][c] < prevHeight:
                return
            visit.add((r,c))

            dfs(r + 1 , c , visit, heights[r][c])
            dfs(r - 1, c , visit, heights[r][c])
            dfs(r , c + 1 , visit, heights[r][c])
            dfs(r , c - 1, visit, heights[r][c])

        
        # 
        for c in range(COLS): 
            dfs(0, c, pac, heights[0][c]) # top row
            dfs(ROWS - 1, c, atl, heights[ROWS-1][c] ) # bottom row

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0]) # first col
            dfs(r, COLS-1, atl, heights[r][COLS-1]) # last col
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res

        