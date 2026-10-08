class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Not unique elements
        # Not unlimited - index keeps incrementing - but how do we prevent duplicates?
        ans = []
        subset = []
        candidates.sort()

        def dfs(i, total):
            if total == target:
                ans.append(subset.copy())
                return
            
            if i == len(candidates) or total > target:
                return
  
            # Backtracking
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                subset.append(candidates[j])
                dfs(j+1, total + candidates[j])
                subset.pop()



        
        dfs(0,0)
        return ans