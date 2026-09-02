class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # I cannot sort the array because I would lose the index
        seen = {}
        for index, number in enumerate(nums):
            difference = target - number
            if difference in seen:
                return [seen[difference], index]
            seen[number] = index
            

        