class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Find a number in the first index of each row that is equal or less than target
        '''
        [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        target=3

        t = 0
        b = 0
        mid = 0

        l=0
        r=3
        middle = 1
        '''
        t = 0
        b = len(matrix)-1

        while t <= b:
            mid = (t + b) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                if matrix[mid][-1] >= target:
                    l = 0
                    r = len(matrix[0])-1
                    while l <= r:
                        middle = (l + r) // 2
                        if matrix[mid][middle] == target:
                            return True
                        elif matrix[mid][middle] < target:
                            l = middle + 1
                        elif matrix[mid][middle] > target:
                            r = middle - 1
                    return False
                else:
                    t = mid + 1
            elif matrix[mid][0] > target:
                b = mid - 1
        return False

