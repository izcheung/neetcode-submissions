class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # Solution 1
        # total = 0
        # for i in range(len(nums) + 1):
        #     total += i
        
        # return total - sum(nums)

        # Solution 2
        total = 0

        for i in range(len(nums) + 1):
            total ^= i

        for num in nums:
            total ^= num

        return total