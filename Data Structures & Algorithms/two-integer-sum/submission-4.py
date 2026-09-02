class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap - number as the key, index as the value
        seen = {}
        # nums = [3,4,5,6], target = 7
        '''
        other 7-3 = 4 ; seen= {3: 0}
        other 7-4 = 3
        '''
        for i in range(len(nums)):
            other = target - nums[i]
            if other in seen:
                return [seen[other], i]
            seen[nums[i]] = i
        return None
            
    