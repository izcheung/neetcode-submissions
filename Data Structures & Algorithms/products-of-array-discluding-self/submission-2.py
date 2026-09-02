class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Get the product of all the numbers
        # Go through the array again and divide the total by the number in the ith position
        total = 1
        zero = []
        for i, num in enumerate(nums):
            if num != 0:
                total *= num
            else:
                zero.append(i)
        if len(zero) > 1:
            return [0] * len(nums)
        elif len(zero) == 1:
            ans = [0] * len(nums)
            ans[zero[0]] = total
            return ans
        else:
            # no zeros
            result = []
            for num in nums:
                curr = total // num
                result.append(curr)
            return result
