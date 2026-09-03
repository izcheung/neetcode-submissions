class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        # [2,3,4,4,5,10,20]
        #             ^
        '''
        ans = 1
        i = 2
        sequence = 4
        max = 4

        '''
        ans = 0
        if len(nums) < 2:
            ans = len(nums)
            return ans
        ans = 1
        i = 0
        sequence = 1
        while i < len(nums)-1: # < 6
            if nums[i+1] == nums[i] + 1:
                sequence += 1
                i += 1
                ans = max(sequence, ans)
            elif nums[i+1] == nums[i]:
                i += 1
            else:
                sequence = 1
                i += 1
         
        return ans

        