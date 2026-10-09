class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # elements are not unique
        # don't have duplicate subsets

        # subsets - unique
        # cannot use multiple - increment the index

        # how to avoid duplicate subsets? sort and skip the same nums

        # Backtracking - take and not take

        ans = []
        subset = []

        nums.sort()

        def dfs(i):
            # Base case
            if i == len(nums):
                ans.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i+1)

            j = i + 1
            while j < len(nums) and j > 0 and nums[j] == nums[j-1]:
                j += 1

            subset.pop()
            dfs(j)
            
        dfs(0)
        return ans



        