class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = nums[0]
        currMin = nums[0]
        res = currMax

        for i in range(1, len(nums)):
            num = nums[i]
            temp = num * currMax
            currMax = max(num, temp, num * currMin)
            currMin = min(num, temp, num * currMin)

            res = max(currMax, res)
        return res
