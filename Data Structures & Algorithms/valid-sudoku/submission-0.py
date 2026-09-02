class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Row
        for i in range(len(board)):
            row = set()
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in row:
                    return False
                row.add(board[i][j])
            row.clear()

        # Column
        for i in range(len(board)):
            column = set()
            for j in range(len(board[0])):
                if board[j][i] == ".":
                    continue
                elif board[j][i] in column:
                    return False
                column.add(board[j][i])
            column.clear()
        
        square = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue    
                row = i // 3
                column = j // 3
                if (row, column) not in square:
                    newSet = set()
                    newSet.add(board[i][j])
                    square[(row, column)] = newSet
                else:
                    if board[i][j] in square[(row, column)]:
                        return False
                    else:
                        square[(row, column)].add(board[i][j])
        
        return True
                    

         
                


        


