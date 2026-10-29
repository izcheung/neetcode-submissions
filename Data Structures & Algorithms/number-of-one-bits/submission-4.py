class Solution:
    def hammingWeight(self, n: int) -> int:
        # Solution 1
        # count = 0
        # while n > 0:
        #     if n % 2 == 1:
        #         count += 1
        #     n = n >> 1
        # return count



        # Solution 2
        count = 0
        while n:
            n = n & (n - 1)
            count += 1
        return count