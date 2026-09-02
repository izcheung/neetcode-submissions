
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
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i >= len(nums):
                return 0
            memo[i] = max(nums[i] + dfs(i+2), dfs(i+1))
            return memo[i]
        return dfs(0)
