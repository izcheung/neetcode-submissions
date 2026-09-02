class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # nlogn
        sortedS = sorted(s)
        sortedT = sorted(t)
        return sortedS == sortedT
