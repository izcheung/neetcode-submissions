class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Unique elements
        # CAN reuse elements

        # Include and exclude dfs backtracking

        ans = []
        subset = []

        # Base case
        def dfs(i, total):
            if total == target:
                ans.append(subset.copy())
                return
            if total > target or i == len(nums):
                return
            
            # Backtracking
            # Include
            subset.append(nums[i])
            dfs(i, total + nums[i])

            # Not include
            subset.pop()
            dfs(i+1, total)
        
        dfs(0, 0)

        return ans