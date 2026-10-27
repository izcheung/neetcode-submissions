class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minCost = 0
        memo = {}

        def dfs(n):
            if n in memo:
                return memo[n]
            # Base Case
            if n < 0:
                return 0
            
            oneStep = dfs(n-1)
            twoStep = dfs(n-2)
            
            # You take the cost at every step
            minCost = min(oneStep, twoStep) + cost[n]
            memo[n] = minCost
            return minCost

        n = len(cost)
        return min(dfs(n-1), dfs(n-2))
