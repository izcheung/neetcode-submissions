class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row = {}
        column = {}
        square = {}

        for i in range(len(board)):
            for j in range(len(board[0])):
                currValue = board[i][j]
                if currValue == ".":
                    continue
                if i not in row:
                    row[i] = set()
                if j not in column:
                    column[j] = set()
                if (i//3, j//3) not in square:
                    square[(i//3,j//3)] = set()

                if (currValue in row[i] or 
                    currValue in column[j] or
                    currValue in square[(i//3 , j//3)]):
                    return False
                else:
                    row[i].add(currValue)
                    column[j].add(currValue)
                    square[(i//3,j//3)].add(currValue)
        return True
                    

         
                


        


