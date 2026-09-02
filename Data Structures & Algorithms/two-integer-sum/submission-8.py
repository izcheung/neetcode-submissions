class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # cannot sort because that changes the indices
        # brute force is having a nested for loop to go over every combination

        for i in range(0, len(nums)-1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
                    

