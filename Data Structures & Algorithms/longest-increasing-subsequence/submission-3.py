class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i, currMax):
            if (i,currMax) in memo:
                return memo[(i,currMax)]
            if i == len(nums):
                return 0
            
            skip = dfs(i+1, currMax)
            take = 0
            if nums[i] > currMax:
                take = 1 + dfs(i+1, nums[i])
            longest = max(skip, take)
            memo[(i,currMax)] = longest
            return longest


        return dfs(0,float('-inf'))

      
