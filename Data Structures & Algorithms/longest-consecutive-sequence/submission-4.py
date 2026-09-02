class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # The order of the original array numbers does not matter, only the number does
        # Sort the array -> do sliding window -> return the maximum length
        # O n(logn)

        [-1,0,1,3,4,5,6,7,8,9]
        [0,1,2,3,4,5,6]
        newNums = sorted(set(nums))
        maxLen = 0
        i = 0
        j = 1
        if len(newNums) < 2:
            return len(newNums)
        while j < len(newNums):
            while j < len(newNums) and newNums[j] == newNums[j-1] + 1:
                j += 1
            maxLen = max(maxLen, j-i)
            i = j
            if j < len(newNums):
                j += 1
         

        return maxLen



        