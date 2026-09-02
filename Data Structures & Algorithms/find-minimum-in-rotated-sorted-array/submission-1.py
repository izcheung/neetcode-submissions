class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        [3,4,5,6,1,2]
    
        while l < r:
            mid = (r + l)//2
            if nums[mid]>nums[r]:
                l = mid + 1
            elif nums[mid]<nums[r]:
                r = mid 
        return nums[l]
            

    
