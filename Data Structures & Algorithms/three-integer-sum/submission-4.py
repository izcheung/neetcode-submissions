class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        # indices don't matter - so you can sort the array from least to most
        nums.sort()

        # Set one number to be constant while the other two numbers are pointers

        '''
        nums=[-2,0,1,1,2]
               i j     k
               total = 0

        '''    
      
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums)-1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    if [nums[i],nums[j],nums[k]] not in ans:
                        ans.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                elif total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
        return ans
                
            
                

        
