class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minCost = 0
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]
            # Base Case
            if i >= len(cost):
                return 0
            
            oneStep = dfs(i+1)
            twoStep = dfs(i+2)
            
            # You take the cost at every step
            minCost = min(oneStep, twoStep) + cost[i]
            memo[i] = minCost
            return minCost

        return min(dfs(0), dfs(1))
