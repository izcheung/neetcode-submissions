class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # key is the number and value is the indices
        for i in range(len(nums)):
            required = target - nums[i]
            if required in seen:

                return [seen[required], i]
            seen[nums[i]] = i

        