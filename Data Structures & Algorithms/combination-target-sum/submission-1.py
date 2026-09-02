class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        max length of nums array
        can the numbers be positive, negative?
        does the order of the numbers matter?

        '''
        res = [] 

        def dfs(i, currArray, total):
            # Base case
            if total == target:
                res.append(currArray.copy())
                return
            if i >= len(nums):
                return
            if total > target:
                return

            # Include the current num
            currArray.append(nums[i])
            dfs(i, currArray, total + nums[i])

            # Not include current num
            currArray.pop()
            dfs(i + 1, currArray, total)

        dfs(0, [], 0)
        return res
