class Solution:
    def solve(self, board: List[List[str]]) -> None:
        border = set()

        def dfs(r,c,seen):
            rowInBounds = 0 <= r < len(board)
            colInBounds = 0 <= c < len(board[0])

            if not rowInBounds or not colInBounds:
                return 
            if board[r][c] == "X":
                return
            if (r,c) in seen:
                return
            seen.add((r,c))
            
            dfs(r+1,c,seen)
            dfs(r-1,c,seen)
            dfs(r,c+1,seen) 
            dfs(r,c-1,seen)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if r == 0 or r == len(board)-1 or c == 0 or c == len(board[0])-1:
                    if board[r][c] == 'O':
                        dfs(r,c,border)


        for r in range(len(board)):
            for c in range(len(board[0])):
                if (r,c) not in border and board[r][c] == 'O':
                    board[r][c] = 'X'
        