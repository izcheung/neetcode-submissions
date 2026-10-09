class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Iterate through the entire board
      

        def dfs(r, c, i, seen):
            rowInBounds = 0 <= r < len(board)
            colInBounds = 0 <= c < len(board[0])
            if not rowInBounds or not colInBounds or (r,c) in seen:
                return False
            if word[i] != board[r][c]:
                return False
            if i == len(word)-1:
                return True

            seen.add((r,c))

    
     
        
            found = (
            dfs(r+1, c, i+1, seen) or 
            dfs(r, c+1, i+1, seen) or 
            dfs(r-1, c, i+1, seen) or 
            dfs(r, c-1, i+1, seen)
            )
            seen.remove((r,c))
            return found

        seen = set()

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0, seen):
                        return True
        return False
                
                
