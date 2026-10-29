class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        memo = {}

        def dfs(i, target):
            if (i,target) in memo:
                return memo[(i,target)]

            if i == len(nums) and target == 0:
                return 1
            if i == len(nums) and target != 0:
                return 0
            
            positive = dfs(i+1, target+nums[i])
            negative = dfs(i+1, target-nums[i])

            res = positive + negative
            
            memo[(i,target)] = res
            return memo[(i,target)]

        return dfs(0, target)