class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        memo = {}
        
        def dfs(i):
            if i in memo:
                return memo[i]

            if i >= len(nums)-1:
                return True
            
            for j in range(1, nums[i]+1):
                if dfs(j + i):
                    return True

            memo[i] = False
            return memo[i]
            
        return dfs(0)