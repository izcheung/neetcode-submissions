class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # cannot sort because that changes the indices so two pointer doesn't really help here
        # brute force is having a nested for loop to go over every combination

        # # O(n2)
        # for i in range(0, len(nums)-1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        # O(n) - compute the second number that I need, and store the number I saw and its index inside a hashmap for o(1) look up
        seen = {}
        for i, num in enumerate(nums):
            needed = target - num
            if needed in seen:
                return [seen[needed], i]
            seen[num] = i


