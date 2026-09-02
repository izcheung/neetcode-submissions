class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #            [1,2,3,4]
        
        # Postfix = 

        # prefixSum = [1] * len(nums)
        prefixSum = [1]
        for i in range(len(nums)-1):
            prevNum = prefixSum[i]
            prefixSum.append(prevNum * nums[i])
        # return prefixSum

        # 1,2,3
        # 0,1,2
        # for i in range(1, len(nums)):
        #     prefixSum[i] *= nums[i-1] * nums
        # return prefixSum
        # Prefix sum [1,1,2,6]n

        postFix = 1
        for j in range(len(prefixSum)-1,-1, -1):
            prefixSum[j] *= postFix 
            postFix *= nums[j]
        return prefixSum

     
        # Answer     [24,12,8,6]

        # Postfix sum[24,12,4,1]

       

