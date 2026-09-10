class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Make it simpler, flatten this 2D array into 1D
        # And then use binary search
        flattenArray =[]
        for array in matrix:
            flattenArray.extend(array)
        l = 0
        r = len(flattenArray)-1

        while l <= r:
            mid = (l+r) // 2
            if flattenArray[mid] == target:
                return True
            elif flattenArray[mid] < target:
                l = mid + 1
            elif flattenArray[mid] > target:
                r = mid - 1
        return False

