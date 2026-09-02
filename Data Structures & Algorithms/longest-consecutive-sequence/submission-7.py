class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        exist = set(nums)
        maxLen = 0
        for number in nums:
            length = 1
            if number - 1 not in exist:
                maxLen = max(maxLen, length)
                nextNum = number
                while nextNum + 1 in exist:
                    length += 1
                    maxLen = max(maxLen, length)
                    nextNum += 1
        return maxLen






        # The order of the original array numbers does not matter, only the number does
        # Sort the array -> do sliding window -> return the maximum length
        # O n(logn)
        # newNums = sorted(set(nums))
        # maxLen = 0
        # i = 0
        # j = 1
        # if len(newNums) < 2:
        #     return len(newNums)
        # while j < len(newNums):
        #     while j < len(newNums) and newNums[j] == newNums[j-1] + 1:
        #         j += 1
        #     maxLen = max(maxLen, j-i)
        #     i = j
        #     if j < len(newNums):
        #         j += 1
         

        # return maxLen



        