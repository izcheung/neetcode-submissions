class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # first column -> first row
        # second column -> second row
        # third column -> third row
        left = 0
        right = len(matrix)-1
        while left < right:
            for i in range(right-left):
                top = left
                bottom = right
                temp = matrix[top][left+i]

                matrix[top][left+i] = matrix[bottom-i][left]

                matrix[bottom-i][left] = matrix[bottom][right-i]

                matrix[bottom][right-i] = matrix[top+i][right]
                
                matrix[top+i][right] = temp
            left += 1
            right -= 1