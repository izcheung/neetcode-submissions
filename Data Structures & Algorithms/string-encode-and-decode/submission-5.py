class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for string in strs:
            encodedString += str(len(string)) + "#" + string
        return encodedString
            

    def decode(self, s: str) -> List[str]:
        # "3#abc5#asdfg"
        i = 0
        ans = []
        while i < len(s):
            number = []
            while i < len(s) and s[i] != "#":
                number.append(s[i])
                i += 1
            i += 1
            currString = []
            end = int("".join(number)) + i
            while i < len(s) and i < end:
                currString.append(s[i])
                i += 1
            ans.append("".join(currString))
        return ans

        



        
        
