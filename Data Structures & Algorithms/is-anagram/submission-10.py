
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # count the number of letters for each string - hashmap
        sDict = {}
        tDict = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)): # s and t length should be same
            sDict[s[i]] = 1 + sDict.get(s[i], 0)
            tDict[t[i]] = 1 + tDict.get(t[i], 0)
        
        return sDict == tDict

        