class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # I can try every combination
        memo = {}
        def dfs(i, amount):
            if (i, amount) in memo:
                return memo[(i,amount)]
            if i >= len(coins) or amount < 0:
                return 0
            if amount == 0:
                return 1

            takeCoin = dfs(i, amount-coins[i])
            dontTake = dfs(i+1, amount)
            memo[(i,amount)]= takeCoin + dontTake
            return memo[(i,amount)]
        return dfs(0,amount)