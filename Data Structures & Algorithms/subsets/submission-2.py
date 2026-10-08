class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Unique elements
        # No reuse

        # 2**n big o
        '''
        Use the include / exclude backtracking method
        The leaf nodes are the subsets possible

        [1]. []
        [1,2] [1] [2] []
        [1,2,3] [1 2] [1, 3] [1] [2,3] [2] [3] []
        '''

        ans = []
        subset = []

        def dfs(i):
            # i represents the index of the array 
            # Base case
            if i == len(nums):
                ans.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        dfs(0)
        return ans


