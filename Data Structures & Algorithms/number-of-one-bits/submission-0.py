class Solution:
    def hammingWeight(self, n: int) -> int:
        # turn into array
        # count number of 1
        string = bin(n)
        count = 0
        for char in string:
            if char == "1":
                count += 1
        return count


        