class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        # total = 1
        # for num in nums:
        #     total *= num
        # for num in nums:
        #     if num !
        #     output.append(total / num)
        # return output
        ans = []
        for i in range(len(nums)):
            total = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                total *= nums[j]
            ans.append(total)
        return ans

