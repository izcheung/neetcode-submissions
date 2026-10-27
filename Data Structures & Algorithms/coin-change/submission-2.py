class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(amount):
            if amount in memo:
                return memo[amount]
            if amount == 0:
                return 0
            if amount < 0:
                return float('inf')
            
            smallest = float('inf')
            for coin in coins:
                smallest = min(1 + dfs(amount-coin), smallest)
            memo[amount] = smallest
            return smallest

        res = dfs(amount)
        if res == float('inf'):
            return -1
        return res
