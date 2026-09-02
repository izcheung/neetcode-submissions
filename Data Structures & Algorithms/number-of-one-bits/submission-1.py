class Solution:
    def hammingWeight(self, n: int) -> int:
        # turn into array
        # count number of 1
        res = 0
        while n > 0:
            res += n % 2
            n = n // 2
        return res


        