class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # use a for loop on the outside for the first number
        # Use a second for loop for the second variable use a hashmap to keep track of what you have seen so far
        result = set()
        nums.sort()
        for i in range(len(nums)):
            seen = {}
            for j in range(i+1, len(nums)):
                need = 0 - nums[i] - nums[j]
                if need in seen:
                    combo = tuple([nums[i], need, nums[j]])
                    if combo not in result:
                        result.add(combo)
                else:
                    seen[nums[j]] = j
        return list(result)
                    
