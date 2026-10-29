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

        for i in range(n+1):
            count = 0
            while i > 0:
                i = i & (i - 1)
                count += 1
            ans.append(count)
        return ans
