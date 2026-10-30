class Solution:
    def countBits(self, n: int) -> List[int]:
        # Solution 1
        # ans = []

        # for i in range(n+1):
        #     count = 0
        #     while i > 0:
        #         if i % 2 == 1:
        #             count += 1
        #         i = i >> 1
        #     ans.append(count)
        # return ans
            
        # Solution 2
        ans = []

        # for i in range(n+1):
        #     count = 0
        #     while i > 0:
        #         i = i & (i - 1)
        #         count += 1
        #     ans.append(count)
        # return ans

        # Solution 3
        dp = [0] * (n + 1)
        ans = [0]
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp