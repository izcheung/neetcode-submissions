class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # all three numbers equal 3 and are all different indices
        # Must sort the array first
        # can use hash map to find the corresponding target value,
        # have a for loop set one of the indices
        # I have to be careful about the any order

        seen = {}
        nums.sort()
        combinations = set()
        ans = []
        for i in range(len(nums)):
            j = i + 1
            k = len(nums)-1
            while j < k:
                total = nums[i] + nums[j] + nums[k] 
                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    combo = tuple([nums[i], nums[j], nums[k]])
                    if combo not in combinations:
                        combinations.add(combo)
                        ans.append([nums[i], nums[j], nums[k]])
                    k -= 1
        return ans
