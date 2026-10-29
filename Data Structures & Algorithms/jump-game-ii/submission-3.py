class Solution:
    def jump(self, nums: List[int]) -> int:
        
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]
                
            if i >= len(nums)-1:
                return 0
            if nums[i] == 0:
                return float('inf')
            
            minJump = float('inf')
            for j in range(1,nums[i]+1):
                minJump = min(1 + dfs(i+j), minJump)
            
            memo[i] = minJump
            return memo[i] 
        
        return dfs(0)