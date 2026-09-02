class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        currSum = 0
        # just have to return the sum
        for num in nums:
            if currSum < 0:
                currSum = 0
            currSum += num
            maxSum = max(maxSum, currSum)
        return maxSum

        