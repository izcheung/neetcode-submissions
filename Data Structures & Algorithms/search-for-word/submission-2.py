class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROWS = len(board)
        COLS = len(board[0])

        visited = set()

        def dfs(r, c, i):
            rowInBounds = 0 <= r < ROWS
            colInBounds = 0 <= c < COLS

            if i == len(word):
                return True
            if not rowInBounds or not colInBounds:
                return False

            if (r,c) in visited:
                return False

      

            if word[i] != board[r][c]:
                return False

          
            
            if word[i] != board[r][c]:
                return False
            
            visited.add((r,c))

            down = dfs(r+1, c, i+1)
            up = dfs(r-1, c, i+1)
            right = dfs(r, c+1, i+1)
            left = dfs(r, c-1, i+1)

            visited.remove((r,c))

            res = down or up or right or left
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False


