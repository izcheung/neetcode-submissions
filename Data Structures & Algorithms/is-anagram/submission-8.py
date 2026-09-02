from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # count the number of letters for each string - hashmap
        return sorted(s) == sorted(t)

        # There is no modifying strings