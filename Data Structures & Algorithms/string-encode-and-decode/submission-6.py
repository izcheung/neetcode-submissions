class Solution:

    def encode(self, strs: List[str]) -> str:
        # You need a number to differentiate between an empty array vs an array with an empty string
        # You need a pound after the number to deal with cases where the string has a length that requires 2 or more digits
        encodedStr = ""
        for string in strs:
            encodedStr += str(len(string)) + "#" + string
        return encodedStr

    def decode(self, s: str) -> List[str]:
        # 3#abc4#abcd
        ans = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            number = int(s[i:j])
            start = j + 1
            end = j + number + 1
            ans.append(s[start: end])
            i = end
        return ans

