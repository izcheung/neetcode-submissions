class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Unique elements
      # CAN reuse - you don't have to increment the index  

        ans = []
        subset = []

        def dfs(i, total):
            # Base case
            if total == target:
                ans.append(subset.copy())
                return
            if total > target:
                return
                
            for j in range(i, len(nums)):
                subset.append(nums[j])
                dfs(j, total + nums[j])
                subset.pop()

        dfs(0,0)
        return ans