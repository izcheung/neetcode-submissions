class Solution:
    def search(self, nums: List[int], target: int) -> int:
   
        '''
        [3,4,5,1,2]
               l  r
        # The lowest number will be on the right (if the mid is part of the left sorted array)

        [1,2,3,4,5]
         l.  m.  r

        [5,1,2,3,4]
         l.r    

        # Use binary search to find the point where it cuts (find the minimum)
        # Use binary search on the two halves to find the target number
        
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
                

        '''

        if len(nums) == 1:
            return 0 if target == nums[0] else -1

        # [3,1]
        # 
        # target=0

        split = (nums[0], 0)
        l = 0
        r = len(nums)-1
        while l <= r:
       
            if nums[l] < nums[r]:
                if nums[l] < split[0]:
                    split = (nums[l], l)
                break
            mid = (l+r) // 2
            if nums[mid] < split[0]:
                split = (nums[mid], mid)
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        
        l2 = 0
        r2 = split[1]-1

        while l2 <= r2:
            mid = (l2 + r2) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l2 = mid + 1
            elif nums[mid] > target:
                r2 = mid - 1
        
        l3 = split[1]
        r3 = len(nums)-1
        
        while l3 <= r3:
            mid = (l3 + r3) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l3 = mid + 1
            elif nums[mid] > target:
                r3 = mid - 1

        return -1



        

















