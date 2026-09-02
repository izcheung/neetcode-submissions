class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1) :
            binaryStr = bin(i)
            count = 0
            for char in binaryStr:
                if char == "1":
                    count += 1
            ans.append(count)
        return ans