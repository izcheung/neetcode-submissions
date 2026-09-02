from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # nlogn
        # sortedS = sorted(s)
        # sortedT = sorted(t)
        # return sortedS == sortedT

        # space n, big o is n using hashmap
        hashS = self.makeHash(s)
        hashT = self.makeHash(t)
        return hashS == hashT

    def makeHash(self, strg):
        newHash = {}
        for char in strg:
            if char not in newHash:
                newHash[char] = 0
            newHash[char] += 1
        return newHash


