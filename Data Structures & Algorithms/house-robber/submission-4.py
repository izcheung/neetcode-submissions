from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        Clarifying question
        - at least one house?
        - all numbers are positive?
        - what is the maximum number of houses?


        [1,1,3,3]
                
        i = 3


        option1 = 3 + dfs(1)
        option2 = dfs(2)


        dfs(1)
        option1 = 1 + 0 = 1
        option2 = dfs(0) = 

        [1,1,8,10,12,1]
        ^.   ^
        





        '''
        # even house indices
        @cache
        def dfs(i):

            if i >= len(nums):
                return 0
            option1 = nums[i] + dfs(i+2)
            option2 = dfs(i+1)
            return max(option1, option2)
        return dfs(0)
