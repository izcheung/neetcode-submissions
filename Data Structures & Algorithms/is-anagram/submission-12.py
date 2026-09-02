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
        hashS = Counter(s)
        hashT = Counter(t)
        return hashS == hashT
