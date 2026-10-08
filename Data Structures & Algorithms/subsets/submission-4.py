class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Use a DFS with for loop / combination backtracking method

        ans = []
        subset = []

        def dfs(i):
            # You add to ans as you come across the subsets 
            # [0,1,2]
            ans.append(subset.copy()) # []
            for j in range(i, len(nums)):
                subset.append(nums[j]) # subset = [0]
                dfs(j+1)
                subset.pop()
        dfs(0)
        return ans