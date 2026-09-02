
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # count the number of letters for each string - hashmap
        sDict = {}
        tDict = {}

        for char in s:
            sDict[char] = 1 + sDict.get(char, 0)
        
        for char in t:
            tDict[char] = 1 + tDict.get(char, 0)

        return sDict == tDict