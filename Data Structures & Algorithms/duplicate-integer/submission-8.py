class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False
        l = 0
        r = 1
        nums.sort() #nlogn
        while r < len(nums):
            if nums[l] == nums[r]:
                return True
            r += 1
            l += 1
        return False