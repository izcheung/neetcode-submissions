class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        total_len = len(board)
        grid = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append(set())
            grid.append(row)

        '''
        ["1","2",".",".","3",".",".",".","."],
        ["4",".",".","5",".",".",".",".","."],
        [".","9","8",".",".",".",".",".","3"],
        ["5",".",".",".","6",".",".",".","4"],
        [".",".",".","8",".","3",".",".","5"],
        ["7",".",".",".","2",".",".",".","6"],
        [".",".",".",".",".",".","2",".","."],
        [".",".",".","4","1","9",".",".","8"],
        [".",".",".",".","8",".",".","7","9"]
        curr_row = 1
        row = {1,}
    
        curr_col = 1
        col = {1, }

        grid 
        '''
        
        for i in range(total_len):
            row = set()
            col = set()
            for j in range(total_len):
                curr_row = board[i][j]
                if curr_row != "." and curr_row in row:
                    return False
                row.add(curr_row)

                curr_col = board[j][i]
                if curr_col != "." and curr_col in col:
                    return False
                col.add(curr_col)

                if curr_row != "." and curr_row in grid[i//3][j//3]:
                    return False
                grid[i//3][j//3].add(curr_row)
        return True



