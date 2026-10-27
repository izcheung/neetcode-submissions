class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i, currMax):
            if (i,currMax) in memo:
                return memo[(i,currMax)]
            if i == len(nums):
                return 0
            
            longest = dfs(i+1, currMax)

            if nums[i] > currMax:
                longest = max(1 + dfs(i+1, nums[i]), longest)
            memo[(i,currMax)] = longest
            return longest


        return dfs(0,float('-inf'))

      
