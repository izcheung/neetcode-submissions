class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        column = len(matrix[0])        
        left = 0
        right = row * column - 1
        while left <= right:
            mid = left + (right - left) // 2
            midElement = matrix[mid//column][mid%column]
            if target == midElement:
                return True
            elif target < midElement:
                right = mid - 1
            elif target > midElement:
                left = mid + 1
        return False