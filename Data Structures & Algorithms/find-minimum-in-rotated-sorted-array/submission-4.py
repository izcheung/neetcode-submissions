class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if l > r: the min is to the right
        l = 0
        r = len(nums)-1
        '''
        [3,4,5,6,1,2]
         l   m     r
        l = 0
        r= 5
        mid = 2

        [3, 0, 1, 2]

        [4,5,0,1,2,3]
             l m   r     


        '''
        mini = float('inf')

        while l <= r:
            if nums[l] < nums[r]:
                mini = min(mini, nums[l])
                break
            mid = (l+r)//2
            mini = min(mini, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return mini
                
