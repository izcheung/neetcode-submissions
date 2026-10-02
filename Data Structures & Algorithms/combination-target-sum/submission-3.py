class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []
        ans = []
        def dfs(i, total):
            if i == len(nums):
                return
            if total > target:
                return
            if total == target:
                ans.append(combinations.copy())
                return
            combinations.append(nums[i])
            dfs(i, total + nums[i])

            combinations.pop()
            dfs(i+1, total)
        dfs(0,0)
        return ans

        # Confused when to increment i, since we can use a number multiple of times