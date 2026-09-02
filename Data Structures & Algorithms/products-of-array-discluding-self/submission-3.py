class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        # Create a prefix product
        '''
        [1,2,4,6]
         ^


        [48,24,6,1]
        48,24,12,8


        # Loop through the nums array
        # Make an array that represents the product of all numbers to the left of the array, and multiply it by the total product of the array divided by the curr number (total product of the array to the right of the number)
            

        total = 48
        [1,2,4,6]
             ^
        total = 48
        left product = [1,1,2,8,48]
                            ^
        right product = []
        ans = [48,24, 
        right product = 48/4=12
        '''
        total = 1
        zero = []
        for i, num in enumerate(nums):
            if num == 0:
                zero.append(i)
            else:
                total *= num
        if len(zero) > 1:
            return [0] * len(nums)
        elif len(zero) == 1:
            ans = [0] * len(nums)
            ans[zero[-1]] = total
            return ans
        else:
            left_product = [1]
            ans = []
            for num in nums:
                left_product.append(left_product[-1] * num)
            for i in range(len(nums)):
                total = total // nums[i]
                ans.append(left_product[i] * total)
        return ans
            
        



