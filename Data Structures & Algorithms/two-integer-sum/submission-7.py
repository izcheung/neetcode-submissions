class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap - number as the key, index as the value
# If i sort it, i should same the num as the first, and the index in the second
        '''
        [2, 3, 3], target = 6
         i j 9
        '''
        numsCopy = []

        for i in range(len(nums)):
            numsCopy.append((nums[i], i))

        numsCopy.sort()

        i = 0
        j = len(nums)-1

        while i < j:
            if numsCopy[i][0] + numsCopy[j][0] == target:
                return [min(numsCopy[i][1],numsCopy[j][1]), max(numsCopy[j][1],numsCopy[i][1] )]
            elif numsCopy[i][0] + numsCopy[j][0] < target:
                i += 1
            else: # > target
                j -= 1
            





            
    