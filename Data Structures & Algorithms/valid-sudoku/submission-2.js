class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board) {

        const col = {}
        const row = {}
        const square = {} // key (r/3, c/3)

        for (let r = 0; r < 9; r++){
            for (let c = 0; c < 9; c++){
                const keySquare = (`${Math.floor(Number(r)/3)},${Math.floor(Number(c)/3)}`)
                if (!(c in col)){
                    col[c] = new Set()
                }
                if (!(r in row)){
                    row[r] = new Set()
                }
                if (!(keySquare in square)){
                    square[keySquare] = new Set()
                }
                const value = board[r][c]

                if (value === ".") continue
                
                if (row[r].has(value) || col[c].has(value) || square[keySquare].has(value)){
                    return false
                }
              
                col[c].add(value)
                row[r].add(value)
                square[keySquare].add(value)
            }

        }
        console.log(col)
        console.log(row)
        console.log(square)
        return true



    }
}
