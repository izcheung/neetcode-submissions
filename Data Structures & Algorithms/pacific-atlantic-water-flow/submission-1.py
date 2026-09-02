class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # start dfs traversal from each valid point that can reach the ocean
        pacific = set()
        atlantic = set()


        def dfs(r, c, visited, prevHeight):

            rowInBound = 0 <= r < len(heights)
            colInBound = 0 <= c < len(heights[0])


            if not rowInBound or not colInBound:
                return

            if (r,c) in visited:
                return

            if heights[r][c] < prevHeight:
                return
            
            visited.add((r,c))

            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])            


        for c in range(len(heights[0])):
            # first row 
            dfs(0, c, pacific, heights[0][c])
            # last row
            dfs(len(heights)-1, c, atlantic, heights[len(heights)-1][c])

        for r in range(len(heights)):
            # first col
            dfs(r, 0, pacific, heights[r][0] )
            # last col
            dfs(r, len(heights[0])-1, atlantic, heights[r][len(heights[0])-1])


        res = []
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r,c])
        return res
