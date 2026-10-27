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
            
            # Take the positive
            positive = dfs(i+1, target+nums[i])
            # Take the negative
            negative = dfs(i+1, target-nums[i])
            memo[(i,target)] = positive + negative
            return memo[(i,target)]

        return dfs(0, target)