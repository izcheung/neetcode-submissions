class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Use a DFS with for loop / combination backtracking method

        ans = []
        subset = []

        def dfs(i):
            # You add to ans as you come across the subsets 
            # [0,1,2]
            if i == len(nums):
                ans.append(subset.copy())
                return 

            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        dfs(0)
        return ans